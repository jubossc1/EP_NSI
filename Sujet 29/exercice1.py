def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre.fg) + taille(arbre.fd)
      
      

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.fg),hauteur(arbre.fd))


