import {
	Button, Form, InputGroup, Modal,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { FaEye, FaPlus } from "react-icons/fa";
import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { encryptWithIV } from "../utils/crypto";
import useAxios from "../utils/useAxios";

export default function PasswordModal() {
	const api = useAxios();
	const [show, setShow] = useState(false);
	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);
	const [showpwd, setShowpwd] = useState("password");
	const history = useHistory();
	const handleSubmit = async (e) => {
		e.preventDefault();
		const encryptedPassword = encryptWithIV(e.target.password.value);
		await api
			.post("/password/add-password/", {
				title: e.target.title.value,
				username: e.target.username.value,
				password: encryptedPassword.password,
				iv: encryptedPassword.iv,
				website: e.target.website.value,
			})
			.then(() => {
				handleClose();
				history.push("/");
				window.location.reload();
			})
			.catch((err) => alert(err.data));
	};
	return (
		<>
			<Modal
				contentClassName="custom-modal"
				id="modal"
				show={show}
				onHide={handleClose}
				align="center"
				centered
				size="lg"
				style={{ fontFamily: "Montserrat" }}
			>
				<Form onSubmit={handleSubmit}>
					<Modal.Header closeButton>
						<Modal.Title className="modal-title">ADD NEW PASSWORD</Modal.Title>
					</Modal.Header>
					<Modal.Body>
						<div align="left">
							<Form.Group className="mb-3" controlId="title">
								<Form.Label className="form-label">Title</Form.Label>
								<Form.Control
									type="text"
									className="text-area"
									placeholder="Enter a title"
									required
								/>
							</Form.Group>
							<Form.Group className="mb-3" controlId="website">
								<Form.Label className="form-label">Website (optional)</Form.Label>
								<Form.Control className="text-area" type="text" placeholder="Enter the web address" />
							</Form.Group>
							<Form.Group className="mb-3" controlId="username" required>
								<Form.Label className="form-label">Username</Form.Label>
								<Form.Control
									type="text"
									className="text-area"
									placeholder="Enter username/email/phone no"
								/>
							</Form.Group>

							<Form.Group className="mb-3" controlId="password">
								<Form.Label className="form-label">Password</Form.Label>
								<Form.Label />
								<InputGroup>
									<Form.Control
										type={showpwd}
										className="text-area1"
										placeholder="Password"
										name="password"
										autoComplete="current-password"
										required
									/>
									<Button
										variant="secondary"
										style={{ width: "2.5rem" }}
										onClick={() => showpwd === "password" ? setShowpwd("text") : setShowpwd("password")}
									>
										<FaEye style={{ marginBottom: 2 }} />
									</Button>
								</InputGroup>
							</Form.Group>
						</div>
					</Modal.Body>
					<Modal.Footer>
						<Button variant="success" type="submit">
              Add
						</Button>
					</Modal.Footer>
				</Form>
			</Modal>

			<div
				className="header-home"
				style={{ paddingTop: "2rem", width: "15rem" }}
			>
				<Button onClick={handleShow} style={{ width: "15rem" }}>
					<FaPlus style={{ marginBottom: 4 }} />
					{" "}
          Add Password
				</Button>
			</div>
		</>
	);
}
