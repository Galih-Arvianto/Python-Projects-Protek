
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print("Daftar Harga Buah")
print ('Apel: 5000'), print ('Jeruk: 8500')
print ('Mangga: 7000'), print ('Duku: 6500')

def Belanja(buahbuah):
    nama = list(buahbuah.keys())
    hargaBuah = tuple(buahbuah.values())

    beli = input('Ingin beli buah apa? : ')
    banyak = int(input('Berapa kilo? : '))
    print('__________________________________')

    urutan = nama.index(beli)
    harga = hargaBuah[urutan] * banyak
    print('Total harga : ' , harga)

Belanja(buah)
