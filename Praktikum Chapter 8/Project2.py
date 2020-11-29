def dataStat(x):
    r=[]
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    r.extend([a,b,c])
    return(a,b,c)
#Menginputkan List
X= int(input('Jumlah bilangan yang ingin dimasukkan = '))
Y=[]
Z=0
for Z in range (X):
    ab = int(input('Masukkan Bilangan = '))
    Y.append(ab)
print(dataStat(Y))