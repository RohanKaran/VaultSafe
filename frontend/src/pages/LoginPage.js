import React, { useContext, useState } from "react";
import { Button, Form } from "react-bootstrap";
import Card from "react-bootstrap/Card";
import { Link } from "react-router-dom";
import { FaEraser, FaSignInAlt } from "react-icons/fa";
import { Logo } from "../components/Logo";
import AuthContext from "../context/AuthContext";

function LoginPage() {
	const { loginUser } = useContext(AuthContext);
	const [value, setValue] = useState({});
	return (
		<div align="center" id="login">
			<Logo />
			<Card>
				<Form
					onSubmit={loginUser}
					onChange={() => setValue(value)}
					onReset={() => setValue({})}
				>
					<div align="left">
						<Form.Group className="mb-3" controlId="formBasicEmail">
							<Form.Label>Email address</Form.Label>
							<Form.Control
								type="email"
								placeholder="Enter email"
								name="username"
								autoComplete="email"
								required
							/>
							<Form.Text className="text-muted">
                We&apos;ll never share your email with anyone else.
							</Form.Text>
						</Form.Group>

						<Form.Group className="mb-3" controlId="formBasicPassword">
							<Form.Label>Password</Form.Label>
							<Form.Control
								type="password"
								placeholder="Password"
								name="password"
								autoComplete="current-password"
								required
							/>
						</Form.Group>
						<Form.Group className="mb-3" controlId="formBasicCheckbox">
							<Form.Check
								type="checkbox"
								label="Remember me"
								name="remember"
							/>
						</Form.Group>
					</div>

					<Button variant="success" type="submit">
						<FaSignInAlt style={{ marginBottom: 4 }} />
						{" "}
            Login
					</Button>
					<Button variant="outline-secondary" type="reset">
						<FaEraser style={{ marginBottom: 4 }} />
						{" "}
            Reset
					</Button>
				</Form>
				<div>
					<Link to="/register">Don&apos;t have an account? Sign up.</Link>
				</div>
			</Card>
		</div>
	);
}

export default LoginPage;
