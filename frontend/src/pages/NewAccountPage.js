import { useHistory, useParams } from "react-router-dom";
import {
	Alert, Button, Card, Form,
} from "react-bootstrap";
import React, { useState } from "react";
import axios from "axios";
import { FaEraser, FaPaperPlane } from "react-icons/fa";
import { Logo } from "../components/Logo";

export function NewAccountPage() {
	const params = useParams();
	const baseURL = process.env.REACT_APP_BACKEND_URL;
	const [alert, setAlert] = useState(null);
	const [variant, setVariant] = useState("danger");
	const history = useHistory();
	const handleSubmit = async (e) => {
		e.preventDefault();
		if (
			e.target.formPassword.value !== e.target.formConfirmPassword.value
		) {
			setVariant("warning");
			setAlert("Passwords do not match.");
			return;
		}
		if (e.target.formPassword.value.length < 6) {
			setVariant("warning");
			setAlert("Password should be grater that 6");
			return;
		}

		await axios
			.post(
				`${baseURL}/user/create/${params.token}/`,
				e.target.formPassword.value,
			)
			.then(() => {
				setVariant("success");
				setAlert("Account created successfully. Redirecting...");
				setTimeout(() => {
					history.push("/login");
				}, 2000);
			})
			.catch((err) => {
				console.log(err.response.data.detail);
				setVariant("danger");
				setAlert("Invalid or expired token.");
			});
	};
	return (
		<div align="center">
			<Logo />
			<Card style={{ width: "20rem", padding: "1rem" }}>
				{alert ? <Alert variant={variant}>{alert}</Alert> : null}
				<Form onSubmit={handleSubmit}>
					<div align="left">
						<Form.Group className="mb-3" controlId="formPassword">
							<Form.Label>Password</Form.Label>
							<Form.Control
								type="password"
								placeholder="***********"
								name="password"
								autoComplete="current-password"
							/>
						</Form.Group>

						<Form.Group className="mb-3" controlId="formConfirmPassword">
							<Form.Label>Confirm Password</Form.Label>
							<Form.Control
								type="password"
								placeholder="***********"
								name="confirm-password"
								autoComplete="confirm-password"
							/>
						</Form.Group>
					</div>

					<Button variant="success" type="submit">
						<FaPaperPlane style={{ marginBottom: 4 }} />
						{" "}
            Submit
					</Button>
					<Button variant="outline-secondary" type="reset">
						<FaEraser style={{ marginBottom: 4 }} />
						{" "}
            Reset
					</Button>
				</Form>
			</Card>
		</div>
	);
}
