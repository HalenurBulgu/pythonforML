
import json

data = '{"ad":"hale","soyad":"bulgu"}'

y=json.loads(data)
print(type(y))
print(y["ad"])

data2 = {
        "hello":"merhaba",
         "goodbye":"hoşçakal"
         }
dataJson = json.dumps(data2)
print(data2)
