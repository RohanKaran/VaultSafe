import {
	Menu,
	MenuItem,
	ProSidebar,
	SidebarContent,
	SidebarFooter,
	SidebarHeader,
	SubMenu,
} from "react-pro-sidebar";
import {
	FaCog,
	FaGithub,
	FaKey,
	FaLock,
	FaPencilAlt,
	FaSignOutAlt,
} from "react-icons/fa";
import { useHistory } from "react-router-dom";
import React, { useContext } from "react";
import { Image } from "react-bootstrap";
import AuthContext from "../context/AuthContext";

export function SideBar() {
	const history = useHistory();
	const { currentUser, logoutUser } = useContext(AuthContext);

	return (
		<ProSidebar id="sidebar-home">
			<SidebarHeader>
				<div align="center" style={{ padding: 10 }}>
					<div>
						<Image
							src="android-chrome-192x192.png"
							style={{ width: "64px", height: "64px", marginTop: 15 }}
						/>
						<span
							style={{ fontFamily: "Abril Fatface", fontSize: "xxx-large" }}
						>
              VaultSafe
						</span>
					</div>
				</div>
			</SidebarHeader>
			<SidebarContent>
				<Menu iconShape="square">
					<MenuItem icon={<FaLock />} onClick={() => history.push("/")}>
            Passwords
					</MenuItem>
					<MenuItem
						icon={<FaPencilAlt />}
						onClick={() => history.push("/notes")}
					>
            Secure Notes
					</MenuItem>
					<SubMenu
						title={(
							<div>
								<div className="text-white" style={{ fontWeight: 500 }}>
									{currentUser?.username}
								</div>
								<div>{currentUser?.email}</div>
							</div>
						)}
						icon={(
							<div style={{ padding: 4 }}>
								<FaCog />
							</div>
						)}
					>
						<MenuItem icon={<FaKey />}>Change Password</MenuItem>
						<MenuItem icon={<FaSignOutAlt />} onClick={logoutUser}>
              Logout
						</MenuItem>
					</SubMenu>
				</Menu>
			</SidebarContent>

			<SidebarFooter>
				<div
					className="sidebar-btn-wrapper"
					style={{padding: "20px 24px",}}
				>
					<a
						href="https://github.com/RohanKaran/VaultSafe"
						target="_blank"
						className="sidebar-btn"
						rel="noopener noreferrer"
					>
						<FaGithub />
						<span
							style={{
								whiteSpace: "nowrap",
								textOverflow: "ellipsis",
								overflow: "hidden",
							}}
						>
                Source Code
						</span>
					</a>
				</div>
			</SidebarFooter>
		</ProSidebar>
	);
}
