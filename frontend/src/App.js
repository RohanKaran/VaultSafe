import React from "react";
import {
	BrowserRouter as Router,
	Redirect,
	Route,
	Switch,
} from "react-router-dom";
import ProtectedRoute from "./utils/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import LoginRoute from "./utils/LoginRoute";
import RegisterPage from "./pages/RegisterPage";
import { NewAccountPage } from "./pages/NewAccountPage";
import { NotePage } from "./pages/NotePage";

function App() {
	return (
		<div>
			<Router>
				<AuthProvider>
					<Switch>
						<ProtectedRoute component={HomePage} path="/" exact />
						<ProtectedRoute component={NotePage} path="/notes" exact />
						<LoginRoute component={RegisterPage} path="/register" exact />
						<LoginRoute component={LoginPage} path="/login" exact />
						<LoginRoute
							component={NewAccountPage}
							path="/new-account/:token"
						/>
						<Route path={"/*"}>
							<Redirect to="/" />
						</Route>
					</Switch>
				</AuthProvider>
			</Router>
		</div>
	);
}

export default App;
