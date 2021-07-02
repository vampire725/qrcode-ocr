#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: Gpp
@File:   app.py
@Time:   2021/6/29 3:02 下午
"""
import io
import pytesseract
import uvicorn

from fastapi import FastAPI
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
from loguru import logger
from starlette.requests import Request

from app.log_set import set_logger

set_logger()
log = logger

app = FastAPI()


@app.post("/api/v1/qrcode", name="二维码识别")
async def qrcode(request: Request) -> dict:
    body = await request.body()
    try:
        ds = decode(Image.open(io.BytesIO(body)), symbols=[ZBarSymbol.QRCODE])
        url = str(ds[0].data, encoding="utf-8") if len(ds) > 0 else ""

    except Exception as e:
        log.error(e)
        url = ""

    return {"url": url}


@app.post("/api/v1/ocr", name="图片识别")
async def orc(request: Request) -> dict:
    body = await request.body()
    try:
        text = pytesseract.image_to_string(Image.open(io.BytesIO(body)), lang="chi_sim")
        text = text.replace("\n", ",").replace(" ", "")
    except Exception as e:
        log.error(e)
        text = ""
    return {"text": text}


@app.get("/health", name="健康检查")
async def health_check() -> str:
    return "ok"


if __name__ == "__main__":
    uvicorn.run("app.start:app", host="0.0.0.0", port=8080, reload=True)
