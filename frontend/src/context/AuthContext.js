import React, { createContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import { useHistory } from "react-router-dom";
import { Alert } from "react-bootstrap";

const AuthContext = createContext();

export default AuthContext;

export function AuthProvider({ children }) {
	const [authTokens, setAuthTokens] = useState(() => (localStorage.getItem("authTokens")
		? JSON.parse(localStorage.getItem("authTokens"))
		: null));
	const [user, setUser] = useState(() => (localStorage.getItem("authTokens")
		? jwt_decode(localStorage.getItem("authTokens"))
		: null));
	const [loading, setLoading] = useState(false);
	const [alert, setAlert] = useState(null);
	const [variant, setVariant] = useState(null);
	const [currentUser, setCurrentUser] = useState(() => (localStorage.getItem("currentUser")
		? JSON.parse(localStorage.getItem("currentUser"))
		: null));

	const history = useHistory();

	const loginUser = async (e) => {
		e.preventDefault();
		setLoading(true);
		await fetch(
			`${process.env.REACT_APP_BACKEND_URL}/user/login/access-token/`,
			{
				method: "POST",
				headers: {
					"Content-Type": "application/x-www-form-urlencoded",
				},
				body: new URLSearchParams({
					username: e.target.username.value,
					password: e.target.password.value,
					grant_type: "password",
				}),
			},
		)
			.then((res) => {
				if (res.status >= 400 && res.status < 600){
					throw new Error("Bad response");
				}
				return res.json();
			})
			.then(async (data) => {
				setAuthTokens({
					access: data.access_token,
					refresh: null,
				});
				localStorage.setItem("authTokens", JSON.stringify({
					access: data.access_token,
					refresh: null,
				}));
				setUser(jwt_decode(data.access_token));

				await fetch(`${process.env.REACT_APP_BACKEND_URL}/user/`, {
					method: "GET",
					headers: { Authorization: `Bearer ${data.access_token}` },
				})
					.then((res) => res.json())
					.then((data) => {
						setCurrentUser(data);
						localStorage.setItem("currentUser", JSON.stringify(data));
						console.log(
							`%cWelcome ${data.username}!`,
							"color: green; font-size: 20px",
						);
					})
					.catch((err) => console.log(err));

				if (e.target.remember.checked) {
					await fetch(
						`${process.env.REACT_APP_BACKEND_URL}/user/login/session-token/`,
						{
							method: "GET",
							headers: { Authorization: `Bearer ${data?.access_token}` },
						},
					)
						.then((res) => res.json())
						.then((data) => {
							const authTemp = JSON.parse(localStorage.getItem("authTokens"));
							authTemp.refresh = data.access_token;
							setAuthTokens(authTemp);
							localStorage.setItem("authTokens", JSON.stringify(authTemp));
						})
						.catch((err) => console.log(err));
				}
			})
			.catch((err) => {
				setVariant("danger");
				setAlert("Invalid email or password!");
				setTimeout(() => {
					setAlert(null);
				}, 2000);
				console.log(err);
			});
	};

	const logoutUser = () => {
		setAuthTokens(null);
		setUser(null);
		setCurrentUser(null);
		localStorage.removeItem("authTokens");
		localStorage.removeItem("currentUser");
		history.push("/login");
	};

	const contextData = {
		user,
		currentUser,
		setCurrentUser,
		authTokens,
		setAuthTokens,
		setUser,
		loginUser,
		logoutUser,
		loading,
	};

	useEffect(() => {
		if (authTokens) {
			setUser(jwt_decode(authTokens.access));
		}
	}, [authTokens]);

	useEffect(()=>{
		if(currentUser){
			setLoading(false);
		}
	}, [currentUser]);

	return (
		<AuthContext.Provider value={contextData}>
			<div align="center">
				{alert ? <Alert variant={variant}>{alert}</Alert> : null}
			</div>
			{children}
		</AuthContext.Provider>
	);
}
