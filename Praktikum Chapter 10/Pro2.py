myfile = open('Pro2.txt', 'r')
ulang = 'y'

while ulang == 'y':
    nim_mhs = input('Masukkan NIM            : ')
    nama_mhs = input('Masukkan Nama Mhs       : ')
    alamat_mhs = input('Masukkan Alamat         : ')
    myfile.write(nim_mhs+'|'+nama_mhs+'|'+alamat_mhs+'\n')
    ulang = input('Ulangi input lagi (y/n) :')

    myfile.close()