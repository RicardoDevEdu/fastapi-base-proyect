import uvicorn
from config.settings import app

if __name__ == "__main__":
    uvicorn.run("config.settings:app", host="0.0.0.0", port=9001, workers=2, reload=True)
