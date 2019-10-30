# How to use

## 起動

```sh
docker-compose up -d # localhost:5001で起動
```

## 終了

```sh
docker-compose down
```

## Base64(PDF) => Base64(PNG)への変換

`localhost:5000/pdf`に`POST`する

### request

```json
{
    "pdf": "base64に変換したpdfに置き換えてください"
}
```

### response

```json
{
  "Base64Images": [
    "1ページ目のpng画像(base64)",
    "2ページ目のpng画像(base64)",
  ],
  "Content-Type": "application/json"
}
```
