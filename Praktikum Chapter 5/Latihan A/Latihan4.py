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
GajiBersih=GajiPokok-(GajiPokok*potongan)
print ("======================================")
print ("==========STRUK GAJI KARYAWAN==========")
print ("--------------------------------------")
print ("Nama karyawan    : "+NamaKaryawan+"(Kode Karyawan:"+KodeKaryawan+")")
print ("Golongan         :   "+Golongan)
print ("--------------------------------------")
print ("Gaji Pokok       :""RP"+ str(GajiPokok))
print ("potongan("+str(potongan*100)+ "%)  : rp" +str(int(GajiPokok*potongan)))
print ("GajiBersih    :Rp"+str(int(GajiBersih)))