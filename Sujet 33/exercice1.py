def taille(arbre:dict, lettre:str):
     x, y = arbre[lettre]
     t = 1
     if x != '':
          t += taille(arbre, x)
     if y != '':
          t += taille(arbre, y)
     return t
