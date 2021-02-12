import json
import requests

temp = []
for count in range(2):
    print(count+1)
    text = json.loads(requests.get("https://tg.i-c-a.su/json/heiyingshabi/"+str(count+1)+"?limit=1000").text)
    for msg in range(len(text["messages"])):
        temp.append(text["messages"][msg]["message"])

temp = [x for x in temp if x != '']
yulu = []
for string in temp:
    yulu.append(string.replace("<br />", ""))

print(json.dumps(yulu, ensure_ascii=False))
