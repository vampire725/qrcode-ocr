# [production]
FROM python:3.9.6-buster

RUN echo >/etc/apt/sources.list "\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\n\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\n\
" && \
apt update && apt install -y sudo vim openssh-server openssh-client libzbar-dev libtesseract-dev tesseract-ocr tesseract-ocr-eng tesseract-ocr-chi-sim

COPY requirements.txt .
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
    pip install --upgrade pip &&\
    pip install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
WORKDIR /usr/src/app/qrcode-ocr
ENV PYTHONPATH=/usr/src/app/qrcode-ocr
COPY . .

ENV TZ="Asia/Shanghai"
LABEL author="gpp" email="guopanpan@sinosoft.com.cn"

CMD [ "python", "app/start.py" ]
