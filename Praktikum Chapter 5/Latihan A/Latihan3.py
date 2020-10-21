NilaiIndo=int(input("berapa nilai Indonya?"))

if (NilaiIndo > 60) and (NilaiIndo <100):
    print ("mantap lulus bahasa,anak sastra ya?")
else:
    print ("waduh sabar bro")


Nilaiipa= int(input("Berapa nilai IPAnya?"))

if (Nilaiipa >60) and (Nilaiipa < 100):
    print ("mantap bang lulus IPA")
else:
    print ("waduh sabar bro")


NilaiMTK=int(input("Berapa nilai MTK nya?"))

if (NilaiMTK > 70) and (NilaiMTK < 100):
    print ("mantap bro lulus mtk luh")
else:
    print ("waduh sabar bro")

if (NilaiIndo>100) or (Nilaiipa>100) or (NilaiMTK>100):
    print ("Maaf input tidak valid")
if (NilaiIndo<0)or (Nilaiipa<0) or (NilaiMTK<0):
    print ("Maaf input tidak valid")
elif (NilaiIndo < 60) or (NilaiMTK < 70) or (Nilaiipa < 60) :
  print("Status Kelulusan              : TIDAK LULUS")
if (NilaiIndo<60):
      print("sebab nilai Indo kurang dari 60")
if (Nilaiipa<60):
      print("sebab nilai IPA kurang dari 60")
if (NilaiMTK<70):
    print ("Sebab nilai MTK kurang dari 70")
else: 
  print("Status Kelulusan              : LULUS")
