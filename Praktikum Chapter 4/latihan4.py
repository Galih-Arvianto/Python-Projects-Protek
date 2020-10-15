jarakAB=125
Vab=62
JarakBC=256
Vbc=70
Hoursberangkat=6
minuteberangkat=0
minuterest=45
longtravel=int(((jarakAB/Vab)+(JarakBC/Vbc))*60)+(minuterest)
jamsampaiC=(longtravel//60)+(longtravel%60)/100+Hoursberangkat
print('pak amir sampai jam'+str(jamsampaiC))