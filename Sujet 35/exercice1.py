def ou_exclusif(tab1,tab2):
    return [tab1[i] ^ tab2[i] for i in range(len(tab1))]


#OU version plus longue/moins complquée

def ou_exclusifV2(tab1,tab2):
    resultat = []
    for i in range(len(tab1)):
        resultat.append(tab1[i]^tab2[i])
      return resultat

        
