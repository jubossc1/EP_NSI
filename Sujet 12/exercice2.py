def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0] * n
    for masse in liste_masses:
        i = 0
        while i <= nb_boites and boites[i] + masse > c:  # Coquille dans le sujet, dans le sujet le c est en majuscule
            i = i + 1
        if i == nb_boites + 1:
            nb_boites += 1
        boites[i] = boites[i] + masse  # Autre coquille dans le sujet, pour que la fonction puisse fonctionner, il faut
                                       # rajouter une indentation par rapport a l'indentation du sujet
    return nb_boites + 1
