import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import {
	Col, Container, Row, Spinner,
} from "react-bootstrap";
import useAxios from "../utils/useAxios";
import "react-pro-sidebar/dist/css/styles.css";
import "../App.css";
import HeaderHome from "../components/HeaderHome";
import { SideBar } from "../components/SideBar";
import NoteCard from "../components/NoteCard";

export function NotePage() {
	const [notes, setNotes] = useState(null);
	const api = useAxios();
	const history = useHistory();

	const getNotes = async () => await api.get("/note/");

	useEffect(() => {
		getNotes()
			.then((r) => setNotes(r.data))
			.catch((e) => {
				if (e.status === 401) {
					history.push("/login");
				}
				console.log(e);
			});
		// eslint-disable-next-line
  }, []);

	return (
		<div>
			<SideBar />
			<Container className="home-container">
				<Row>
					<Col id="main-home">
						<HeaderHome />
						{notes ? (
							notes?.length > 0 ? (
								notes.map((note) => <NoteCard key={note.id} note={note} />)
							) : (
								<Container className="text-secondary">
    No Notes to display. Please add a note.
								</Container>
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
