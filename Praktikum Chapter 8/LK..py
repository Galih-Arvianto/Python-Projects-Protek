#LK1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('List A:',a)
print('List B:',b)

#LK2
a.insert (3,10)
b.insert (2,15)
print ('List A ver1',a)
print ('List B ver1',b)

#LK3
a.append(4)
b.append(8)
print ('List A ver2',a)
print ('List B ver2',b)

#LK4
a.sort()
b.sort()
print('List urut A Ver2',a)
print('List urut B Ver2',b)

#LK5
c = a[:8]
d = b[2:10]
print('List C:',c)
print('List D:',d)

#LK6
e = []
for x in range(len(c)):
    e += [c[x]+d[x]]
print('List E:',e)

#LK7
e = (tuple(e))
print('List E (tuple)', e)

#LK8
print('Nilai min list E:',min(e))
print('Nilai max list E:',max(e))
print('Hasil Jumlah list E:',sum(e))

#LK9
myString = "python adalah bahasa pemrograman yang menyenangkan"

#LK10
myString = set(myString)
print(myString)

#LK11
myString = list(myString)
myString.sort()
print('Urutan alfabet kata mystring:',myString)