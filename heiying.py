import json
import requests

text = requests.get("https://tg.i-c-a.su/json/heiyingshabi?limit=1000").text
text = json.loads(text)
yulu = []
for msg in range(len(text["messages"])):
    yulu.append(text["messages"][msg]["message"])
yulu = [x for x in yulu if x != '']
print(json.dumps(yulu, ensure_ascii=False))
