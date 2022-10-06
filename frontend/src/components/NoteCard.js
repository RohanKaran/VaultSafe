import {
	Button,
	Col,
	Collapse,
	Container,
	Form,
	Image,
	Modal,
	Row,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import {
	FaEye, FaEyeSlash, FaPencilAlt, FaTrashAlt,
} from "react-icons/fa";
import React, { useState } from "react";
import useAxios from "../utils/useAxios";
import { encrypt, decrypt } from "../utils/crypto";

export default function NoteCard(props) {
	const [show, setShow] = useState(false);
	const [open, setOpen] = useState(false);
	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);
	const [showupdate, setShowupdate] = useState(false);
	const handleCloseUpdate = () => setShowupdate(false);
	const handleShowUpdate = () => setShowupdate(true);
	const api = useAxios();
	const Update = async (e) => {
		e.preventDefault();
		await api
			.put(`note/update/${props.note.id}/`, {
				title: e.target.title.value,
				content: encrypt(e.target.note.value),
			})
			.then(() => {
				handleCloseUpdate();
				window.location.reload();
			})
			.catch((err) => console.log(err.data));
	};
	const Delete = async () => {
		await api
			.delete(
				`${
					`${process.env.REACT_APP_BACKEND_URL
					}/note/delete/${
						props.note.id
					}/`
				}`,
			)
			.then(() => {
				handleClose();
				window.location.reload();
			})
			.catch((err) => console.log(err));
	};
	return (
		<div className="password-card" style={{ borderRadius: "10px", boxShadow: "0px 0px 4px 4px rgb(129, 130, 129)" }}>
			<div>
				<Modal
					contentClassName="custom-modal"
					id="modal"
					show={showupdate}
					onHide={handleCloseUpdate}
					align="center"
					centered
					size="lg"
					style={{ fontFamily: "Poppins, sans-serif" }}
				>
					<Form onSubmit={Update}>
						<Modal.Header closeButton>
							<Modal.Title style={{ fontFamily: "Poppins, sans-serif", fontWeight: "bold" }}>UPDATE NOTE</Modal.Title>
						</Modal.Header>
						<Modal.Body>
							<div align="left">
								<Form.Group className="mb-3" controlId="title">
									<Form.Label>Title</Form.Label>
									<Form.Control
										type="text"
										placeholder="Enter a title"
										defaultValue={props.note.title}
										required
									/>
								</Form.Group>
								<Form.Group className="mb-3" controlId="note">
									<Form.Label>Note</Form.Label>
									<Form.Control
										type="textarea"
										placeholder="Enter your note"
										required
										as="textarea"
										rows={6}
										defaultValue={decrypt(props.note.content)}
									/>
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
				<Modal.Header style={{ fontFamily: "Poppins, sans-serif", fontWeight: "bold" }} closeButton>DELETE NOTE</Modal.Header>
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
					<Col>
						<Row  style={{ alignItems: "center" }}>
							<Col xs="auto">
								<div style={{ paddingRight: 0, marginRight: 0 }}>
									<Image
										src="favicon.ico"
										width="20rem"
										style={{ paddingRight: 0, marginRight: 0 }}
									/>
								</div>
							</Col>
							<Col
								style={{fontSize: "max(2vw, 20px)", fontWeight: "500"}}
							>
								{props.note.title}
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
									<FaPencilAlt 
										style={{ marginBottom: 4 }}
										className="text-success"
									/>
								</Button>
								<Button
									onClick={() => setOpen(!open)}
									aria-controls="example-collapse-text"
									aria-expanded={open}
									className="bg-transparent"
									variant="outline-dark"
									style={{ float: "right", marginRight: "1rem", border: "none" }}
								>
									<div className="text-dark">
										{open ? (
											<FaEyeSlash style={{ marginBottom: 4 }} />
										) : (
											<FaEye style={{ marginBottom: 4 }} />
										)}
									</div>
								</Button>
							</Col>
						</Row>
						<Row>
							<Col>
								<div>
									<Collapse in={open}>
										<div id="example-collapse-text" style={{ left: "2.8rem", position: "relative" }}>
											{decrypt(props.note.content)}
										</div>
									</Collapse>
								</div>
							</Col>
						</Row>
					</Col>
				</Row>
			</Container>
		</div>
	);
}
