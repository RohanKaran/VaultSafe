import CryptoJS from "crypto-js";

const secret = process.env.REACT_APP_SECRET1_KEY;
const key = CryptoJS.enc.Hex.parse(secret);

export const encryptWithIV = (password) => {
	const iv = CryptoJS.lib.WordArray.random(128 / 8);

	const encryptedPassword = CryptoJS.AES.encrypt(password, key, {
		iv,
		mode: CryptoJS.mode.CTR,
		padding: CryptoJS.pad.AnsiX923,
	});
	return {
		iv: encrypt(iv.toString(CryptoJS.enc.Hex)),
		password: encryptedPassword.toString(),
	};
};

export const decryptWithIV = (encryption) => {
	const decryptedPassword = CryptoJS.AES.decrypt(encryption.password, key, {
		iv: CryptoJS.enc.Hex.parse(decrypt(encryption.iv)),
		mode: CryptoJS.mode.CTR,
		padding: CryptoJS.pad.AnsiX923,
	});

	return decryptedPassword.toString(CryptoJS.enc.Utf8);
};

export const encrypt = (iv) => {
	const encryptedIv = CryptoJS.AES.encrypt(iv, process.env.REACT_APP_SECRET2_KEY);
	return encryptedIv.toString();
};

export const decrypt = (encryptedIv) => {
	const iv = CryptoJS.AES.decrypt(encryptedIv, process.env.REACT_APP_SECRET2_KEY);
	return iv.toString(CryptoJS.enc.Utf8);
};
