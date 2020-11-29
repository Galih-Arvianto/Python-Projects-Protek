Nama = []
X = 1

while True :
    print('Masukan nama ' + str(X) + ' : ' )
    x = str(input())
    Nama.append(x)
    lanjut = str(input('lagi ? (y/n): ' ))
    if lanjut == 'y' :
        True
    elif lanjut == 'n' :
        break
    else :
        print('Inputan valid')
    X = X + 1

Nama.sort()

for x in range(len(Nama)):
    print(Nama[x], '(', len(Nama[x]), 'Karakter )')