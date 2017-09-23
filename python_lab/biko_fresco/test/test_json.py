import json

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
data['dsad'] = 43244
data['dsdad'] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
json1 = json.dumps(data)
print(json1)
