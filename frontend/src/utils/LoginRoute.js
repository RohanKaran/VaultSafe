import { Redirect, Route } from "react-router-dom";
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

function LoginRoute({ children, ...rest }) {
	const { user } = useContext(AuthContext);
	return <Route {...rest}>{user ? <Redirect to="/" /> : children}</Route>;
}

export default LoginRoute;
