import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import {
	Col, Container, Row, Spinner,
} from "react-bootstrap";
import useAxios from "../utils/useAxios";
import PasswordCard from "../components/PasswordCard";
import "react-pro-sidebar/dist/css/styles.css";
import "../App.css";
import HeaderHome from "../components/HeaderHome";
import { SideBar } from "../components/SideBar";

function HomePage() {
	const [passwords, setPasswords] = useState(null);
	const api = useAxios();
	const history = useHistory();

	useEffect(() => {
		const getPasswords = async () => await api
			.get("/password/")
			.then((r) => setPasswords(r.data))
			.catch((e) => {
				if (e.status === 401 || e.status === 403) {
					history.push("/login");
				}
				console.log(e);
			});
		getPasswords();
		// eslint-disable-next-line
  }, []);

	return (
		<div>
			<SideBar />
			<Container className="home-container">
				<Row>
					<Col id="main-home">
						<HeaderHome />
						{passwords ? (
							passwords.length <= 0 ? (
								<Container className="text-secondary">
									No password to display. Please add a password.
								</Container>
							) : (
								passwords.map((password) => (
									<PasswordCard key={password.id} password={password}/>
								))
							)
						) : (
							<Container>
								<Spinner animation="border" variant="primary" />
							</Container>
						)}
					</Col>
				</Row>
			</Container>
		</div>
	);
}

export default HomePage;
