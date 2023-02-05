def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
        un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)
