#Assez dur comme exo

def ajoute_dictionnaires(d1:dict,d2:dict):
    if d1 == {}:
        return d2
    elif d2 == {}:
        return d1

    d = dict()
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1 == k2:
                a = d1[k1] + d2[k2]
                d[k1] = a
            else:
                if k1 not in d or k2 not in d:
                    d[k1] = d1[k1]
                    d[k2] = d2[k2]

    return d
  
