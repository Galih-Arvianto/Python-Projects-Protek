n = int(input('Tentukan jumlah bilangan bulat yang ingin dimasukkan : '))
bil = []
for a in range(n):
    a = int(input('Masukkan bilangan bulat : '))
    bil.append(a)
bil.sort()
bil.reverse()
print(bil)