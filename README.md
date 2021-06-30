# qrcode-ocr

二维码识别和图片识别文字服务

# 构建镜像

```bash
docker build -t qrcode-ocr:1.0 .
```

# docker 启动

```bash
docker run -it -d --name qrcode-ocr -p 8082:8080 qrcode-ocr:1.0
```

# 访问swagger接口页面

```http request
http://127.0.0.1:8082/docs
```