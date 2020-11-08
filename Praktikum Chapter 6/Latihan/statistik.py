def sum(*SemuaAngka):
    total = 0
    for number in SemuaAngka:
        total += number
    return total

def average(*SemuaAngka):
    average = 0
    for number in SemuaAngka:
        average+= 1
    return sum(*SemuaAngka) / average

def max(*SemuaAngka):
    max = SemuaAngka[0]
    for number in SemuaAngka:
        if(number > max):
            max = number
    return max

def min(*SemuaAngka):
    min = SemuaAngka[0]
    for number in SemuaAngka:
        if(number < min):
            min = number
    return min