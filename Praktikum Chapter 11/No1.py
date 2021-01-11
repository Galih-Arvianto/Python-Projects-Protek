from datetime import *


def diffDate(x):
    sekarang=datetime.now()
    a=datetime.date(datetime.now())
    print('Tanggal hari: ',a)
    jumlah=datetime.strptime(x, '%Y-%m-%d')
    selisih=sekarang-jumlah
    selisihari=abs(selisih.days)
    return selisihari

t='2018-12-30'
print(diffDate(t))