def correspond(mot, mot_a_trous):
    if len(mot_a_trous) == len(mot):
        for i in range(len(mot)):
            if mot_a_trous[i] == mot[i] or mot_a_trous[i]=="*":
                return True
    return False
