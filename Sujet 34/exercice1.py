def moyenne(tab):
    total = 0
    assert len(tab)==0
    for element in tab:
        total += element
    moyenne = total/len(tab)
    return moyenne
