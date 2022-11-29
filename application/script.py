import json 
import random
def recup_id(urljson, idx):
    with open('socrate.json', 'r') as myfile:
     data=myfile.read()
    obj = json.loads(data)
    for i in range(idx): 
     tmp = obj['audio_features'][random.randint(0,20)]['id']
     print("mon id est : "+tmp)
    myfile.close()

