nama = input("Masukkan nama file: ")
try:
    file = open(nama, "a")
    file.write(input("Data yang mau ditambahkan: "))
    Add = input("Mau lagi (y/n) : ")
    while (Add == 'y'):
        file.write(input("Data yang mau ditambahkan: "))
        Add = input("Mau lagi (y/n) : ")
    if (Add == 'n'):
        file.close()
except FileNotFoundError:
    print("File Tidak Ada")
except ValueError:
    print('Input tidak valid')