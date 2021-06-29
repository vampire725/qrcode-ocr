# [production]
FROM 192.168.129.112:10001/zkr-env-python:3.8-buster

COPY requirements.txt .
RUN apt install libzbar-dev
#sudo apt update
#sudo apt install tesseract-ocr
#sudo apt install libtesseract-dev
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
    pip install --upgrade pip &&\
    pip install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /usr/src/app/qrcode-ocr
ENV PYTHONPATH=/usr/src/app/qrcode-ocr
COPY . .

ENV TZ="Asia/Shanghai"
LABEL author="gpp" email="guopanpan@sinosoft.com.cn"

CMD [ "python", "app/start.py" ]
