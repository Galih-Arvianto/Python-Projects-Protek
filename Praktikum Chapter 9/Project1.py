def ubah(teks, a, b):
    A = list(teks)
    hasil = '' 
    
    for i in A:
        if i == a:
            i = b
        hasil = ''.join([hasil,i])
    return hasil

n = ubah('MATEMATIKA','T','S')
print(n)