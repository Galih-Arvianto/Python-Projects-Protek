KodeKaryawan= input("Kode Karyawannya brp?")
NamaKaryawan= input("Nama Karyawan siapa?")
Golongan= input("Golongan berapa?")

if(Golongan=="A"):
    GajiPokok=int(10000000)
    potongan=float(0.025)
if(Golongan=="B"):
    GajiPokok=int(8500000)
    potongan=float(0.02)
if(Golongan=="C"):
    GajiPokok=int(7000000)
    potongan=float(0.015)
if(Golongan=="D"):
    GajiPokok=int(5500000)
    potongan=float(0.01)
#Tunjangan
StatKaryawan= input("Masukkan Status (1:menikah, 2:Belum): ")
if(StatKaryawan == "1"):
  status = "Sudah Menikah"
  tunNikah = 0.1
  anak = input("Masukkan jumlah anak : ")
  tunAnak = int(anak) * 0.05
elif(StatKaryawan == "2"):
  status = "Belum Menikah"
  tunNikah = 0
  anak = "0"
  tunAnak = 0

GajiKotor=GajiPokok+(GajiPokok * tunAnak)+(GajiPokok * tunNikah)
GajiBersih=GajiKotor-(GajiPokok*potongan)

print ("======================================")
print ("==========STRUK GAJI KARYAWAN==========")
print ("--------------------------------------")
print ("Nama karyawan    : "+NamaKaryawan+"(Kode Karyawan:"+KodeKaryawan+")")
print ("Golongan         :   "+Golongan)
print ("Status Nikah     : "+status)
print ("Jumlah anak      :"+anak)
print ("--------------------------------------")
print ("Gaji Pokok       :""RP"+ str(GajiPokok))
print ("Tunjangan Nikah  :"+str(int(GajiPokok*tunNikah)))
print ("Tunjangan Anak   :"+str(int(GajiPokok*tunAnak)))
print ("__________________________________________+")
print ("Gaji Kotor       :Rp"+str(int(GajiKotor)))
print ("potongan("+str(potongan*100)+ "%)  : rp" +str(int(GajiPokok*potongan)))
print ("__________________________________________-")
print ("GajiBersih    :Rp"+str(int(GajiBersih)))