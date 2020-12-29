myfile = open('Pro2.txt', 'r')
list_data = myfile.readlines()
i = 0
new_list = []
for data in list_data:
    data_mhs = str(list_data[i])
    data_mhs = data_mhs.split('|')
    new_list.append(data_mhs)
    i += 1

dataMahasiswa = {}
A = 0
for datas in new_list:
    M = {}
    M['nama'] = new_list[A][1]
    M['nim'] = new_list[A][0]
    M['alamat'] = str.rstrip(new_list[A][2])
    dataMahasiswa[str(A+1)] = M    
    A += 1

print(dataMahasiswa)