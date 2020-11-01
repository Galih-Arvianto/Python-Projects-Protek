def factorial(n):
    if (n == 0):
        return 1
    else :
        return n * factorial(n-1)

def COMB(a, b):
    hasil = factorial(a) / (factorial(a-b)*factorial(b))
    print(hasil)

def PERM(a, b):
    hasil = factorial(a)/factorial(a-b)
    print(hasil)

#3A
COMB(5,3)

#3B
PERM(10,7)