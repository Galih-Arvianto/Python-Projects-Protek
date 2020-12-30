myfile = open('Pro2.txt', 'r')
f=input('Masukkan NIM :')
x=0
n=0
for i in myfile:
    b=i.split('|')
    c=b[0]
    d=b[1]
    e=b[2]
    dataMahasiswa={'nim':c,'nama':d,'alamat':e}
    if f==dataMahasiswa['nim']:
        print('Data Mahasiswa:')
        print('NIM : ', dataMahasiswa['nim'])
        print('Nama :', dataMahasiswa['nama'])
        print('Alamat : ', dataMahasiswa['alamat'])
        myfile.close()
        break
if f !=dataMahasiswa['nim']:
    print('Data tidak ditemukan')
    myfile.close()