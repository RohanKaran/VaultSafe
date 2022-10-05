import uvicorn  # pyright: reportMissingTypeStubs=false
from app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app, debug=True, log_level="debug"
    )  # pyright: reportGeneralTypeIssues=false
