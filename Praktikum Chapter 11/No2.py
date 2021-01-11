from datetime import *
pinjam = datetime.date(datetime.now())
kembali = pinjam + timedelta(days = 7)
myfile = open('DataPem.txt', 'w')
lanjut = 'y'
while lanjut == 'y':
    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku : ")
    pinjam = date.today()
    kembali = pinjam + timedelta(days = 7)
    data = [kode, nama, judul, str(pinjam), str(kembali) + '\n']
    myfile.write('|'.join(data))
    a = input("\nUlangi lagi (y/n) : ")
    if(a.lower() == 'y') :
        continue
    elif(a.lower() == 'n') :
        break
    else :
        print("ulangi!")
        break

myfile.close()
    