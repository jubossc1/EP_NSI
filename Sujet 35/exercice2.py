def est_semimagique(self):
    s = self.somme_ligne(0)
    #test de la somme de chaque ligne
    for i in range(self.ordre):
        if self.somme_ligne(i) != s:
            return False
    #test de la somme de chaque colonne
    for j in range(self.ordre):
        if self.somme_col(j) != s:
            return False
    return True

