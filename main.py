import uvicorn
from config.settings import app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9001, reload=True, workers=2)
