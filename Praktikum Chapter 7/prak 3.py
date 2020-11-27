file=open ("D:data.txt", "r")
sum=0
for data in file:
    try:
        sum=sum+int (data)
    except ValueError:
        print('Value Invalid')

print (sum)
