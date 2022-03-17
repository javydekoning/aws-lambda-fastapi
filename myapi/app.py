import os
import json
from anyio import sleep

from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="MyAwesomeApp")

num = 10
for x in range(num):
    print('Initializing... Sleeping 1s')
    sleep(1)


@app.get("/Prod")
def hi():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "You've hit / on the RED/GREEN API. Try /red or /green",
        }),
    }


@app.get("/red")
def hello_red():
    return {
        "statusCode": 200,
        "body": "You've hit 🟥 ",
    }


@app.get("/green")
def hello_green():
    return {
        "statusCode": 200,
        "body": "You've hit 🟩 ",
    }


@app.get("/{proxy}")
def hi(proxy: str):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "You've hit /" + proxy + " Why not try /red or /green",
        }),
    }


lambda_handler = Mangum(app)
