'''import selenuim'''
from selenium import webdriver

def recup_titre(url:str):
    '''Ouvre un site et Recupère son titre'''
    driver = webdriver.Chrome()
    driver.get(url)
    titre = driver.title
    driver.close()
    return titre

def compare_titre(titre_1,titre_2,titre_3):
    '''Renvoi la plus Grande Chaine'''
    if len(titre_1)<len(titre_2):
        if len(titre_2)<len(titre_3):
            return titre_3
        return titre_2
    if len(titre_1)<len(titre_3):
        return titre_3
    return titre_1

if __name__ == '__main__':
    site1= recup_titre("https://stackoverflow.com/")
    site2=recup_titre("https://openclassrooms.com/")
    site3=recup_titre("https://github.com/")
    print(compare_titre(site1,site2,site3))
