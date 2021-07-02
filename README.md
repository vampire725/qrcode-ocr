# qrcode-ocr

二维码识别和图片识别文字服务

- [qrcode-ocr](#qrcode-ocr)
  - [使用](#使用)
    - [构建镜像](#构建镜像)
    - [启动服务](#启动服务)
      - [docker run 启动](#docker-run-启动)
      - [docker-compose 启动](#docker-compose-启动)
    - [访问swagger接口页面](#访问swagger接口页面)

## 使用

### 构建镜像

```shell script
docker build -t qrcode-ocr:1.0 .
```

### 启动服务

#### docker run 启动

```shell script
docker run -it -d --name qrcode-ocr -p 8080:8080 qrcode-ocr:1.0
```

#### docker-compose 启动

```shell script
docker-compose up -d
```

### 访问swagger接口页面

```http request
http://127.0.0.1:8082/docs
```
