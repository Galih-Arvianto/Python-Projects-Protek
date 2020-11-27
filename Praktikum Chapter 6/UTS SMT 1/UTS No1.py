def BodyMassIndex (BMI):
    if (BMI<18):
        statusTubuh='KURUS'
    elif (BMI>=18) and (BMI<23):
        statusTubuh='IDEAL'
    elif (BMI>=23) and (BMI<27):
        statusTubuh='GEMUK'
    elif (BMI>=27) and (BMI<35):
        statusTubuh='OBESITAS'
    else:
        statusTubuh='MORBID'
    return statusTubuh

input(int(berapa)