import uvicorn  # pyright: reportMissingTypeStubs=false

from app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app, debug=True, host="0.0.0.0", port=5004, log_level="debug"
    )  # pyright: reportGeneralTypeIssues=false
