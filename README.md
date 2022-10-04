# VaultSafe

## Setup and run

To setup the project locally 
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

  For Linux Users:
```
source ./venv/Scripts/activate
```
  For Windows Command Line Users:
```
venv\Scripts\activate
```

3. Install all the dependencies in `requirements.txt` file:
```
pip install -r requirements.txt
```

4. Make sure you create `.env` using `.env.template` in both frontend and backend directories.

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
cd ..
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
