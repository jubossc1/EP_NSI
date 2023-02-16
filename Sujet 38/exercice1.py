def correspond(mot:str, mot_a_trou:str):
    if len(mot) == len(mot_a_trou):
        for i in range(len(mot)):
            if mot[i] != mot_a_trou[i] and mot_a_trou[i] != "*":
                return False
        return True
    return False

