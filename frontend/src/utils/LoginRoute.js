import { Navigate } from "react-router-dom";
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

function LoginRoute({ children }) {
	const { user } = useContext(AuthContext);
	if (user) {
		return <Navigate to="/" replace />;
	}
	return children;
}

export default LoginRoute;
