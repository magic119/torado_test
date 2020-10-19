import json

data = {"name": "徐红涛"}

json_data = json.dumps(data)

print(json_data)

print(json.loads(json_data))

print(r"\u5f90".encode(encoding="utf-8"))