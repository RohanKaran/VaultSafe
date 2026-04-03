import uvicorn  # pyright: reportMissingTypeStubs=false
from app import create_app
from app.core import config

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        log_level="debug",
        reload=config.DEBUG,
    )  # pyright: reportGeneralTypeIssues=false
