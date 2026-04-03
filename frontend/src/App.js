import React from "react";
import {
	BrowserRouter as Router,
	Navigate,
	Route,
	Routes,
} from "react-router-dom";
import ProtectedRoute from "./utils/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import LoginRoute from "./utils/LoginRoute";
import RegisterPage from "./pages/RegisterPage";
import { NewAccountPage } from "./pages/NewAccountPage";
import { NotePage } from "./pages/NotePage";

export default function App() {
	return (
		<div>
			<Router>
				<AuthProvider>
					<Routes>
						<Route path="/" element={<ProtectedRoute><HomePage /></ProtectedRoute>} />
						<Route path="/notes" element={<ProtectedRoute><NotePage /></ProtectedRoute>} />
						<Route path="/register" element={<LoginRoute><RegisterPage /></LoginRoute>} />
						<Route path="/login" element={<LoginRoute><LoginPage /></LoginRoute>} />
						<Route path="/new-account/:token" element={<LoginRoute><NewAccountPage /></LoginRoute>} />
						<Route path="*" element={<Navigate to="/" replace />} />
					</Routes>
				</AuthProvider>
			</Router>
		</div>
	);
}
