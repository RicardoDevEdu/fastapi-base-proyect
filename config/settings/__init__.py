
import sentry_sdk
from fastapi import FastAPI
from littlenv import littlenv
from fastapi.middleware.cors import CORSMiddleware

from config import urls
from config.settings.base import (
    API_VERSION,
    SENTRY,
    APP_NAME,
    APP_DESCRIPTION,
    connect_db, 
    close_db
)


try:
    littlenv.load()
except:
    pass


itemsInit = {}


sentry_sdk.init(
    SENTRY,
    traces_sample_rate=1.0
)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=API_VERSION,
    redoc_url="/api/v1/redoc",
    docs_url='/api/v1/docs',
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    urls.urls
)

app.add_event_handler(
    "startup",
    connect_db
)


app.add_event_handler(
    "shutdown",
    close_db
)





