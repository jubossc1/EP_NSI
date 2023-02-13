#Solution incorrect (par karl)
def correspond(mot, mot_a_trous):
    if len(mot_a_trous) == len(mot):
        for i in range(len(mot)):
            if mot_a_trous[i] == mot[i] or mot_a_trous[i]=="*":
                return True
    return False

#Solution fonctionnel
def correspond(mot:str, mot_a_trou:str):
    if len(mot) == len(mot_a_trou):
        for i in range(len(mot)):
            if mot[i] != mot_a_trou[i] and mot_a_trou[i] != "*":
                return False
        return True
    return False

