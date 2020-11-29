
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print("Daftar Harga Buah")
print ('Apel: 5000 '), print ('Jeruk: 8500')
print ('Mangga: 7000'), print ('Duku: 6500')

totalharga=0
while True:
    nama=str(input('Beli buah apa? :'))
    if nama in buah:
        jumlah=float(input('Berapa Kilo?:'))
        total=jumlah*buah[nama]
        totalharga+=total
        lagi=str(input('Ingin buah yang lainnya? (y/n)?: '))
        if (lagi=='y'):
            continue
        elif(lagi=='n'):
            print('Total harga =',totalharga)
            break
    else:
        print('Buah kosong')