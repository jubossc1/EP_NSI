ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            print(position_alphabet(c))
            indice = (int(position_alphabet(c))+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat
