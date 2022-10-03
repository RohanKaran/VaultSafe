import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { Col, Row } from "react-bootstrap";
import PasswordModal from "./PasswordModal";
import NoteModal from "./NoteModal";

export default function HeaderHome() {
	return (
		<Row>
			<Col xs="auto">
				<PasswordModal />
			</Col>
			<Col xs="auto">
				<NoteModal />
			</Col>
		</Row>
	);
}
