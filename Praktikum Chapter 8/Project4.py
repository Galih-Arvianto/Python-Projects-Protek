#List Sayur awal
Sayur = ['bayam', 'kangkung', 'wortel', 'selada']
#--------------------------------------------------
print('Sayur ada : Bayam,Kangkung,Wortel dan Selada')
print('Menu Option List:')
print('A. Tambah list Sayur')
print('B. Hapus list Sayur')
print('C. Tampilkan list Sayur')
while True:
    option=input('Ingin apa(A/B/C)? = ') 
    if (option=='A'):
        tambah=input('Masukkan sayur yang ingin ditambah = ')
        Sayur.append(tambah)
        print('Data Sayur =', Sayur)
    elif (option=='B'):
        hapus=input('Masukkan sayur yang ingin dihapus = ')
        if hapus in Sayur:
            Sayur.remove(hapus)
            print('Data Sayur =', Sayur)
        else:
            print('Data Sayur Tidak Ditemukan')
    elif (option=='C'):
        print('Data Sayur =', Sayur)
        lagi=input('ingin mengubah(y/n)?')
        if (lagi=='y'):
            continue
        elif (lagi=='n'):
            break