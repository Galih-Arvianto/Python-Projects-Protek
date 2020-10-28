from random import randint
print('"Hai.. nama saya Mr.Lappie, saya telah memilih sebuah bilanga bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!" ')

Nyawa=100
while True :
    bil = randint(0, 100)
    ans = int(input('Tebakan Anda = '))
    if (Nyawa==0):
        print ("Ups Nyawa abizzzzzzz") 


    if(ans > bil):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
        Nyawa-=2
    elif(ans < bil):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
        Nyawa-=2
    elif (ans == bil):
        print('Yeeee... Bilangan tebakan anda BENAR :-)')
        break

print ('Skor anda adalah :'+Nyawa)