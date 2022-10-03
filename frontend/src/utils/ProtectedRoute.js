import { Redirect, Route } from "react-router-dom";
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

function ProtectedRoute({ children, ...rest }) {
	const { user } = useContext(AuthContext);
	return <Route {...rest}>{!user ? <Redirect to="/login" /> : children}</Route>;
}

export default ProtectedRoute;
