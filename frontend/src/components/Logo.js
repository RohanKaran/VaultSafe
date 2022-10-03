import React from "react";
export function Logo() {
	return (
		<div style={{ margin: 30, height: "60px" }}>
			<img
				src="../android-chrome-192x192.png"
				style={{ verticalAlign: "middle", margin: 5, width: "60px" }}
				alt="logo"
			/>
			<span
				style={{
					fontFamily: "Abril Fatface",
					fontSize: "xxx-large",
					verticalAlign: "middle",
					height: "60px",
					textAnchor: "middle",
				}}
			>
        VaultSafe
			</span>
		</div>
	);
}
