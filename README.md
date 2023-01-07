![ESLint](https://github.com/RohanKaran/VaultSafe/actions/workflows/eslint.yml/badge.svg)
![CodeQL](https://github.com/RohanKaran/VaultSafe/actions/workflows/codeql.yml/badge.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![ReactJS](https://img.shields.io/badge/Frontend-ReactJS-blue)

# VaultSafe
VaultSafe is a website where users can store passwords and notes securely. It uses [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) to encrypt the data. 

⭐ the repo if you like it.

## Tech Stack
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Frontend: [ReactJS](https://reactjs.org/docs/getting-started.html)
- UI: [React-Bootstrap](https://react-bootstrap.github.io)

## Setup and run

To set up the project locally 
1. [Fork the repo](https://github.com/RohanKaran/VaultSafe/fork)
2. Then clone the repo in your local system
```
git clone https://github.com/YOUR_USERNAME/VaultSafe
```
Detailed Tutorial:
1. https://docs.github.com/en/get-started/quickstart/fork-a-repo
2. https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### Backend
The project runs on Python 3.

1. Create virtual environment:
```
cd backend
virtualenv venv
```

2. Activate virtual environment:
- For Linux Users:
```
source ./venv/bin/activate
```
- For Windows Command Line Users:
```
venv\Scripts\activate
```

3. Install all the dependencies in `requirements.txt` file:
```
pip install -r requirements.txt
```

4. Make sure you create `.env` using `.env.template` in both frontend and backend directories. <strong>(important)</strong>

5. Create a user:
```
python initial_data.py
```

6. Run the backend:
```
python main.py
```

### Frontend
7. Move to frontend directory:
```
cd frontend
```

8. Install all the dependencies using npm:
```
npm install
```
9. Start the server:
```
npm start
```

- If you are facing any problem setting up the project locally ask [here](https://github.com/RohanKaran/VaultSafe/discussions/new?category=q-a)

### Default Local Credentials
- Email: `user@example.com`
- Password: `localpassword`

<br/>

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=2db859a6e9f9&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
