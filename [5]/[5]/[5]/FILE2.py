# write objects to the file in json format, then display the result.
import json, os

fo = open("json-text.json", "wb+")
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
fo.write(json.dumps(x).encode())
fo.close()
del fo

fo = open("json-text.json", "r")
for x in fo:
    output = json.loads(x)
fo.close()
print(json.dumps(output,indent=4))