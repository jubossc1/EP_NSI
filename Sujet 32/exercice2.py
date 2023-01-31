class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis coeur, carreau et trèfle. """
        self.contenu = [Carte(i,j) for i in range(1,5) for j in range(1,14)]

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos
        (entier compris entre 0 et 51). """
        assert 0 <= pos <= 51
        valeur = self.contenu[pos].get_valeur()
        couleur = self.contenu[pos].get_couleur()
        return Carte(couleur, valeur)
