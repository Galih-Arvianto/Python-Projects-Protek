#A--------------------------------------------------------

print ('JAWABAN A')
from operation import *
a=2
b=4
c=6
d=4
e=b*c
f=e+a

print(b, 'x', c, '=' ,kali(b,c))
print(a, '+', e, '=' ,jumlah(a,e))
print(f, '-', d, '=' ,kurang(f,d))

#B--------------------------------------------------------

print ('JAWABAN B')
from operation import*
a=4
b=7
c=6
d=9
e=a+b
f=c-d

print(a, '+', b, '=' ,jumlah(a,b))
print(c, '-', d, '=' ,kurang(c,d))
print(e, 'x', f, '=' ,kali(e,f))

#C------------------------------------------------------------------------------------------
print ('Jawaban C')
from operation import*
a=10
b=2
c=7
d=5
e=12
f=34
P1=a+b
P2=c+d
P3=e-f
P4=P1/P2

print(a, '+', b, '=' ,jumlah(a,b))
print(c, '+', d, '=' ,jumlah(c,d))
print(e, '-', f, '=' ,kurang(e,f))
print(P1, '/', P2,'=' ,bagi(P1,P2))
print(P3, '/', P4,'=' ,bagi(P3,P4))

