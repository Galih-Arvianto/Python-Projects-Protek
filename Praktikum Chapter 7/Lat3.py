print ('-----------------------------')
print ('---PROGRAM HITUNG RATA RATA---')
print ('-----------------------------')

#-------------------------
A=0
Awal=0
def masukan():
    try:
        global A
        global Awal
        global ulangi
        bil = float(input('Masukkan bilangan bulat :    '))
        ulangi = input(str('Lagi     (y/n) ? : '))
        Awal += bil
        A += 1
    except ValueError:
        print("Bukan bilangan bulat")
while True:
    masukan()
    if ulangi=='n':
        break
print ('-----------------------------')
mean = Awal/A
print('Rata - ratanya adalah : ', mean)