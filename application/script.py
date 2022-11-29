import json 
import random

with open('socrate.json', 'r') as myfile:
 data=myfile.read()
obj = json.loads(data)
for i in range(10): 
tmp = obj['audio_features'][random.randint(0,20)]['id']
print("mon id est : "+tmp)
myfile.close()

