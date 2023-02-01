#Si on a le droit au slicing
def multiplication(a:int, b:int):
    tot = 0
    if a < 0:
        a = int(str(a)[1:])
        tot += 1
    if b < 0:
        b = int(str(b)[1:])
        tot += 1
    x = 0
    for i in range(b):
        x += a
    if tot == 1:
        return int("-" + str(x))
    return x
  
#Sinon
def multiplication(a:int, b:int):
    tot = 0
    if a < 0:
        a = a - (a + a)
        tot += 1
    if b < 0:
        b = b - (b + b)
        tot += 1
    x = 0
    for i in range(b):
        x += a
    if tot == 1:
        return x - (x + x)
    return x
