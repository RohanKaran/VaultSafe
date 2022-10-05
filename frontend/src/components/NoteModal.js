import { Button, Form, Modal } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { FaPlus } from "react-icons/fa";
import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { encrypt } from "../utils/crypto";
import useAxios from "../utils/useAxios";

export default function NoteModal() {
	const api = useAxios();
	const [show, setShow] = useState(false);
	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);
	const history = useHistory();
	const handleSubmit = async (e) => {
		e.preventDefault();
		await api
			.post("/note/add-note/", {
				title: e.target.title.value,
				content: encrypt(e.target.note.value),
			})
			.then(() => {
				handleClose();
				history.push("/notes");
				window.location.reload();
			})
			.catch((err) => console.log(err.data));
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
						<Modal.Title className="modal-title">NEW NOTE</Modal.Title>
					</Modal.Header>
					<Modal.Body>
						<div align="left">
							<Form.Group className="mb-3" controlId="title">
								<Form.Label className="form-label">Title</Form.Label>
								<Form.Control
									className="text-area"
									type="text"
									placeholder="Enter a title"
									required
								/>
							</Form.Group>
							<Form.Group className="mb-3" controlId="note">
								<Form.Label className="form-label">Note</Form.Label>
								<Form.Control
									type="textarea"
									placeholder="Enter your note"
									required
									as="textarea"
									rows={6}
								/>
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
			<div className="header-home" style={{ paddingTop: "2rem" }}>
				<Button onClick={handleShow} style={{ width: "15rem" }}>
					<FaPlus style={{ marginBottom: 4 }} />
					{" "}
          Add Note
				</Button>
			</div>
		</>
	);
}



