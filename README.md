# VaultSafe

## Setup and run

To setup the project locally read these wiki pages and follow the instructions:

### Backend
The project runs on Python 3.

1. Create and activate virtual environment:
```
cd backend
virtualenv venv
```
For Linux Users:
```
source ./venv/Scripts/activate
```
For Windows Command Line Users:
```
venv\Scripts\activate
```

2. Install all the dependencies in `requirements.txt` file:
```
pip install -r requirements.txt
```

4. Make sure you create `.env` using `.env.template` in both frontend and backend directories.

5. Run the backend:
```
python main.py
```

### Frontend
6. Move to frontend directory:
```
cd ..
cd frontend
```

7. Install all the dependencies using npm:
```
npm install
```
8. Start the server:
```
npm start
```
