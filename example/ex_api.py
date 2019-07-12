import json
import requests



# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
# Print the status code of the response.

print("url: url属性")
print(response.url)
print("ステータスコード: status_code属性")
print(response.status_code)
print("エンコーディング: encoding属性")
print(response.encoding)
print("レスポンスヘッダ: headers属性")
print(response.headers)
print("テキスト: text属性")
print(response.text)
print("バイナリデータ: content属性")
print(response.content)
