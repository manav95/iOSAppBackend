import requests
import json

data = {"data" : [[5,2,3,1,2],[4,4,2,2,1],[2,6,7,3,1],[1,2,3,4,5],[0,56,33,22,14]]}
r = requests.post('http://127.0.0.1:9875/recordData', json=json.dumps(data))
print r.text
a = requests.get('http://127.0.0.1:9875/recordData')
print a.text
v = requests.get('http://127.0.0.1:9875/trainingData')
print v.json
