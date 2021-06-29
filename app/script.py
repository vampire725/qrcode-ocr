#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: Gpp
@File:   script.py
@Time:   2021/6/29 6:14 下午
"""

import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("1.png"))
print(text)
