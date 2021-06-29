#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: Gpp
@File:   app.py
@Time:   2021/6/29 3:02 下午
"""
import io
import pytesseract

from flask import Flask, jsonify
from flask import request
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
from loguru import logger

from app.log_set import set_logger

set_logger()
log = logger

app = Flask(__name__)


@app.route("/api/v1/qrcode", methods=["POST"])
def qrcode():
    try:
        ds = decode(
            Image.open(io.BytesIO(request.get_data())), symbols=[ZBarSymbol.QRCODE]
        )
        url = str(ds[0].data, encoding="utf-8") if len(ds) > 0 else ""

    except Exception as e:
        log.error(e)
        url = ""

    return {"url": url}


@app.route("/api/v1/ocr", methods=["POST"])
def orc():
    try:
        text = pytesseract.image_to_string(Image.open(io.BytesIO(request.get_data())))
    except Exception as e:
        log.error(e)
        text = ""
    return {"text": text}


@app.route("/health", methods=["POST", "GET"])
def health_check():
    return "ok"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False,
    )
