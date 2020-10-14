import math
jarakAB=125
Vab=62
JarakBC=256
Vbc=70
berangkat=6
rest=45/60
sampaiC=math.floor((berangkat+(jarakAB/Vab)+(JarakBC/Vbc)+rest)*60)
jamsampaiC=math.floor(sampaiC/60)
menitsampaic=jamsampaiC%60
print('Pak Amir tibat ke kota c pada pukul'+str(jamsampaiC)+'lebih'+str(menitsampaic)+ 'menit')