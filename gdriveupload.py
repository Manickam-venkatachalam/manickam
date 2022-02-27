import json
import requests
headers = {"Authorization": "Bearer ya29.A0ARrdaM8osZPdYf57ftir9DzewH9H8RufyJj-GAsSkO0bgFinaerX-wNNgtSeJJvIKcfGRpoIXSTd_LFunSOWvMYVf9LC0SqAC6sKvBjD5eWFgfy_-hJchSrNcqzuqjYaG5Lx1RO7XojAbgJFuNAsr6gaMbsv"}
para = {
    "name": "bacholer.mkv",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./bacholer.mkv", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)