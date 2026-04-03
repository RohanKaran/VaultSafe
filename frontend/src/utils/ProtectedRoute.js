import { Navigate } from "react-router-dom";
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

function ProtectedRoute({ children }) {
	const { user } = useContext(AuthContext);
	if (!user) {
		return <Navigate to="/login" replace />;
	}
	return children;
}

export default ProtectedRoute;
