'''import ressources'''
import json
import random
from termcolor import colored

colors = ['green',"red","blue","yellow"]

def lireligne (idx, col):
    '''method liregligne to json'''
    with open('application/socrate.json' , 'r', encoding='utf-8') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    myfile.close()
    tmp = obj['audio_features'][idx][col]
    print(colored(tmp, colors[random.randint(0,3)]))
    return tmp

if __name__ == '__main__':
    for i in range(10):
        lireligne(random.randint(0,50),"id")
    