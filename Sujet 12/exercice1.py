#Class créé a partir des données de l'énoncé, pas demandé dans l'exercice
class ABR:

    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self.gauche is not None:
            g = repr(self.gauche)
        else:
            g = "None"
        if self.droit is not None:
            d = repr(self.droit)
        else:
            d = "None"
        return "(" + g + "," + str(self.cle) + "," + d + ")"


#Fonction demandé dans l'exercice      
def ajoute(x, abr):
    val = abr.cle
    if val == x:
        return abr
    elif val > x:
        if abr.gauche is None:
            n = ABR(None, x, None)
            return ABR(n, val, abr.droit)
        else:
            return ABR(ajoute(x, abr.gauche), val, abr.droit)
    else:
        if abr.droit is None:
            n = ABR(None, x, None)
            return ABR(abr.gauche, val, n)
        else:
            return ABR(abr.gauche, val, ajoute(x, abr.droit))
