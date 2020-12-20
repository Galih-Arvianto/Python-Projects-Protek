import random

def shufflestring(x,n):
    result=[]
    if n > 2*len(x):
        n=(len(x)*2)
        print('Random : ', n)
    while n > 0 :
        acak = random.sample (x, len(x))
        result1 = ''.join(acak)
        if (result1 in result)==True:
            n+=1
        if (result1 in result)==False:
            result.append(result1)
        n -= 1
    print(result)

shufflestring('aku',100);