def ou_exclusif(tab1,tab2):
    return [tab1[i] ^ tab2[i] for i in range(len(tab1))]

