from random import randint

def lancer(n:int):
    tab = []
    for i in range(n):
        tab.append(randint(1, 6))
    return tab

def paires_6(tab:list):
    tot = 0
    for i in tab:
        if i == 6:
            tot += 1
            if tot >= 2:
                return True
    return False
