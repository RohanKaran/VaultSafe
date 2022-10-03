module.exports = {
	"env": {
		"node": true,
		"browser": true,
		"es2021": true
	},
	"extends": [
		"eslint:recommended",
		"plugin:react/recommended"
	],
	"overrides": [
	],
	"parserOptions": {
		"ecmaVersion": "latest",
		"sourceType": "module"
	},
	"plugins": [
		"react"
	],
	"settings": {
		"react": {
			"createClass": "createReactClass",
			"pragma": "React",  // Pragma to use, default to "React"
			"fragment": "Fragment",  // Fragment to use (maybe a property of <pragma>), default to "Fragment"
			"version": "detect",
			"flowVersion": "0.53" // Flow version
		},
	},
	"rules": {
		"indent": [
			"error",
			"tab"
		],
		"linebreak-style": [
			"error",
			"unix"
		],
		"quotes": [
			"error",
			"double"
		],
		"semi": [
			"error",
			"always"
		],
		"react/prop-types": 0,
		"react/no-unknown-property": ["error", { ignore: ["align"] }]
	}
};
