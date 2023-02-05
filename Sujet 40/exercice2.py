class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None


    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si le sous-arbre droit est non
     vide
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si le sous-arbre gauche est non
        vide
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

#À compléter à partir d'ici      
      
    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de
        recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.valeur :
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on recommence le test
                self.gauche.inserer(cle)

            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            # on insère à droite
            if self.droitExiste():
                # on descend à droite et on recommence le test
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)

