  
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def termahal(harga):
    change= list(harga.values())
    change.sort()
    change.reverse()
    r=change[0]
    for x,y in harga.items():
        if(y==r):
            return x
    return r


print(termahal(buah))
