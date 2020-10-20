NilaiIndo=int(input("berapa nilai Indonya?"))

if (NilaiIndo >= 60) and (NilaiIndo <= 100):
    print ("mantap lulus bahasa,anak sastra ya?")
else:
    print ("waduh sabar bro")

Nilaiipa= int(input("Berapa nilai IPAnya?"))
if (Nilaiipa >= 60) and (Nilaiipa <= 100):
    print ("mantap bang lulus IPA")
else:
    print ("waduh sabar bro")

NilaiMTK=int(input("Berapa nilai MTK nya?"))
if (NilaiMTK >= 70) and (NilaiMTK <= 100):
    print ("mantap bro lulus mtk luh")
else:
    print ("waduh sabar bro")

if (NilaiIndo <60 ) or (Nilaiipa <60) or (NilaiMTK <70):
    print ("Status kelulusan: Tidak Lulus")
else:
    print ("Status kelulusan: Lulus")