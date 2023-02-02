def tri_selection(tab):
     N = len(tab)
     for k in range(N):
          imin = k
          for i in range(k, N):
               if tab[i] < tab[imin]:
                    imin = i
          tab[k] , tab[imin] = tab[imin] , tab[k]
          
