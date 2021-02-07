import json
import requests

text = requests.get("https://tg.i-c-a.su/json/heiyingshabi?limit=1000").text
text = json.loads(text)
temp = []
for msg in range(len(text["messages"])):
    temp.append(text["messages"][msg]["message"])
temp = [x for x in temp if x != '']
yulu = []
for string in temp:
    yulu.append(string.replace("<br />", ""))
print(json.dumps(yulu, ensure_ascii=False))
