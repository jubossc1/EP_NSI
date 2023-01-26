def mini(t_moy, annees):
    mi = t_moy[0]
    an = 0
    for i in range(len(t_moy)):
        if t_moy[i] < mi:
            mi = t_moy[i]
            an = i
    return(mi, annees[an])
  
