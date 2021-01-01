myfile = open('Pro5A.txt', 'r')
list_data = myfile.readlines()
i = 0
listb = []
for data in list_data:
    Angka = str(list_data[i])
    Angka = Angka.split('|')
    listb.append(Angka)
    i += 1

newfile = open('Pro5B.txt', 'w')
a = 0
for A in listb:
    A1 = int(listb[a][0])
    A2 = int(listb[a][1])
    newfile.write(str(A1+A2)+'\n')
    a += 1