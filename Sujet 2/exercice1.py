def indices_maxi(tab:list):
    max = tab[0]
    indices = []
    for i in range(len(tab)):
        if tab[i] == max:
            indices.append(i)
        elif tab[i] > max:
            max = tab[i]
            indices = [i]
    return max, indices
  
