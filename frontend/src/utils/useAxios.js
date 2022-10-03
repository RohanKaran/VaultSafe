import axios from "axios";
import jwt_decode from "jwt-decode";
import dayjs from "dayjs";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const baseURL = process.env.REACT_APP_BACKEND_URL;

const useAxios = () => {
	const {
		authTokens, setUser, setCurrentUser, setAuthTokens,
	} = useContext(AuthContext);

	const axiosInstance = axios.create({
		baseURL,
		headers: { Authorization: `Bearer ${authTokens?.access}` },
	});

	axiosInstance.interceptors.request.use(async (req) => {
		const user = jwt_decode(authTokens.access);
		const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

		if (!isExpired) return req;

		if (authTokens.refresh) {
			await axios
				.get(`${baseURL}/user/refresh-token/${authTokens.refresh}/`)
				.then(async (response) => {
					authTokens.access = response.data.token;
					localStorage.setItem("authTokens", JSON.stringify(authTokens));
					setUser(jwt_decode(response.data.token));

					await fetch(`${process.env.REACT_APP_BACKEND_URL}/user/`, {
						method: "GET",
						headers: { Authorization: `Bearer ${response.data.token}` },
					})
						.then((res) => res.json())
						.then((data) => {
							setCurrentUser(data);
							localStorage.setItem("currentUser", JSON.stringify(data));
						})
						.catch((err) => console.log(err));

					req.headers.Authorization = `Bearer ${response.data.token}`;
					return req;
				})
				.catch((err) => {
					setAuthTokens(null);
					setUser(null);
					setCurrentUser(null);
					localStorage.setItem("authTokens", null);
					localStorage.setItem("currentUser", null);
					console.log(err);
					return req;
				});
			return req;
		}

		setAuthTokens(null);
		setUser(null);
		setCurrentUser(null);
		localStorage.setItem("authTokens", null);
		localStorage.setItem("currentUser", null);
		return req;
	});

	return axiosInstance;
};

export default useAxios;
