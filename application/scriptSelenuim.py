from selenium import webdriver

def recup_titre(url:str):
    '''Ouvre un site et Recupère son titre'''
    driver = webdriver.Chrome()
    driver.get(url)
    titre = driver.title
    driver.close()
    return titre


def compareTitre(t1,t2,t3):
    '''Renvoi la plus Grande Chaine'''
    if len(t1)<len(t2):
        if len(t2)<len(t3):
            return t3
        else:
            return t2
    else:
        if len(t1)<len(t3):
            return t3
        else:
            return t1

if __name__ == '__main__':
    site1= recup_titre("https://stackoverflow.com/")
    site2=recup_titre("https://openclassrooms.com/")
    site3=recup_titre("https://github.com/")
    print(compareTitre(site1,site2,site3))