def fusion(tab1:list, tab2:list):
    new_tab = []
    for i in range(len(tab1) + len(tab2)):
        if tab1 == []:
            for i in tab2:
                new_tab.append(i)
                return new_tab
        elif tab2 == []:
            for i in tab1:
                new_tab.append(i)
                return new_tab
        else:
            if tab1[0] < tab2[0]:
                new_tab.append(tab1[0])
                del tab1[0]
            else:
                new_tab.append(tab2[0])
                del tab2[0]
