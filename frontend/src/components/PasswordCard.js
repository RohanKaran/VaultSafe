import {
	Button,
	Col,
	Container,
	Form,
	Image,
	InputGroup,
	Modal,
	Row,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import {
	FaEye, FaEyeSlash, FaPencilAlt, FaTrashAlt,
} from "react-icons/fa";
import React, { useEffect, useState } from "react";
import { decryptWithIV, encryptWithIV } from "../utils/crypto";
import useAxios from "../utils/useAxios";

export default function PasswordCard(props) {
	const defaultPassword = "★★★★★★";
	const [password, setPassword] = useState(defaultPassword);
	const [src, setSrc] = useState("android-chrome-192x192.png");
	const [show, setShow] = useState(false);
	const [showpwd, setShowpwd] = useState("password");
	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);
	const [showupdate, setShowupdate] = useState(false);
	const handleCloseUpdate = () => setShowupdate(false);
	const handleShowUpdate = () => setShowupdate(true);
	const api = useAxios();
	const Update = async (e) => {
		e.preventDefault();
		const encryptedPassword = encryptWithIV(e.target.password.value);
		await api
			.put(`/password/update/${props.password.id}/`, {
				title: e.target.title.value,
				username: e.target.username.value,
				password: encryptedPassword.password,
				iv: encryptedPassword.iv,
				website: e.target.website.value,
			})
			.then(() => {
				setShow(false);
				window.location.reload();
			});
	};

	const Delete = async () => {
		await api
			.delete(
				`${
					`${process.env.REACT_APP_BACKEND_URL
					}/password/delete/${
						props.password.id
					}/`
				}`,
			)
			.then(() => {
				handleClose();
				window.location.reload();
			})
			.catch((err) => console.log(err));
	};
	useEffect(() => {
		if (props.password.website) {
			if (props.password.website.startsWith("http")) setSrc(`${props.password.website}/favicon.ico`);
			else setSrc(`https://${props.password?.website}/favicon.ico`);
		}
		// eslint-disable-next-line
  }, []);
	return (
		<div className="password-card" style={{ borderRadius: "10px", boxShadow: "0px 0px 4px 4px rgb(129, 130, 129)" }}>
			<div>
				<Modal
					id="modal"
					contentClassName="custom-modal"
					show={showupdate}
					onHide={handleCloseUpdate}
					align="center"
					centered
					size="lg"
					style={{ fontFamily: "Poppins, sans-serif" }}
				>
					<Form onSubmit={Update}>
						<Modal.Header closeButton>
							<Modal.Title style={{ fontFamily: "Poppins, sans-serif", fontWeight: "bold" }}>UPDATE PASSWORD</Modal.Title>
						</Modal.Header>
						<Modal.Body>
							<div align="left">
								<Form.Group className="mb-3" controlId="title">
									<Form.Label>Title</Form.Label>
									<Form.Control
										type="text"
										placeholder="Enter a title"
										required
										defaultValue={props.password?.title}
									/>
								</Form.Group>
								<Form.Group className="mb-3" controlId="website">
									<Form.Label>Website (optional)</Form.Label>
									<Form.Control
										type="text"
										placeholder="Enter the web address"
										defaultValue={props.password?.website}
									/>
								</Form.Group>
								<Form.Group className="mb-3" controlId="username" required>
									<Form.Label>Username</Form.Label>
									<Form.Control
										type="text"
										placeholder="Enter username/email/phone no"
										defaultValue={props.password?.username}
									/>
								</Form.Group>

								<Form.Group className="mb-3" controlId="password">
									<Form.Label>Password</Form.Label>
									<Form.Label />
									<InputGroup>
										<Form.Control
											type={showpwd}
											placeholder="Password"
											name="password"
											autoComplete="current-password"
											defaultValue={decryptWithIV({
												password: props.password.password,
												iv: props.password.iv,
											})}
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
							<Button variant="success rounded-2" type="submit">
                Update
							</Button>
						</Modal.Footer>
					</Form>
				</Modal>
			</div>
			<Modal
				id="modal"
				show={show}
				onHide={handleClose}
				align="center"
				centered
				size="md"
				style={{ fontFamily: "Poppins, sans-serif" }}
			>
				<Modal.Header style={{ fontFamily: "Poppins, sans-serif", fontWeight: "bold" }} closeButton>DELETE PASSWORD</Modal.Header>
				<Modal.Body>
					<div style={{ fontSize: "2rem" }}>Are you sure?</div>
          This action cannot be undone.
				</Modal.Body>
				<Modal.Footer>
					<Button variant="danger rounded-2" onClick={Delete}>
            Yes
					</Button>
					<Button variant="outline-secondary rounded-2" onClick={handleClose}>
            Cancel
					</Button>
				</Modal.Footer>
			</Modal>

			<Container>
				<Row>
					<Col xs="auto">
						<div style={{ paddingRight: 0, marginRight: 0 }}>
							<Image
								src={src}
								width="90rem"
								style={{ paddingRight: 0, marginRight: 0 }}
								onError={() => setSrc("android-chrome-192x192.png")}
							/>
						</div>
					</Col>
					<Col>
						<Row>
							<Col>
								<div
									style={{fontSize: "large", fontWeight: "500"}}
								>
									{props.password.title}
								</div>

								<div className="text-secondary" style={{ marginTop: -8 }}>
									<small>{props.password.website}</small>
								</div>
							</Col>
							<Col>
								<Button
									style={{ float: "right", border: "none" }}
									className="bg-transparent"
									onClick={handleShow}
									variant="outline-danger"
								>
									<FaTrashAlt
										style={{ marginBottom: 4 }}
										className="text-danger"
									/>
								</Button>
								<Button
									style={{ float: "right", marginRight: "1rem", border: "none" }}
									onClick={handleShowUpdate}
									variant="outline-success"
									className="bg-transparent"
								>
									<FaPencilAlt className="text-success" style={{ marginBottom: 4 }} />
								</Button>
							</Col>
						</Row>
						<Row>
							<Col>
                Username : {props.password.username}
							</Col>
						</Row>
						<Row>
							<Col>
                Password : {password}
							</Col>
							<Col xs="auto">
								<button
									style={{ float: "right" }}
									className="bg-transparent border-0"
									onClick={() => {
										if (password === defaultPassword) {
											setPassword(
												decryptWithIV({
													password: props.password.password,
													iv: props.password.iv,
												}),
											);
										} else setPassword(defaultPassword);
									}}
								>
									{password === defaultPassword ? (
										<FaEye style={{ marginBottom: 4 }} />
									) : (
										<FaEyeSlash style={{ marginBottom: 4 }} />
									)}
								</button>
							</Col>
						</Row>
					</Col>
				</Row>
			</Container>
		</div>
	);
}
