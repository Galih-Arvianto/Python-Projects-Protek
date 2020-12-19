def StarB(n):
    A = 0
    B = 1
    while A < n/2 :
        star = '*' * B
        A += 1
        B += 2
        print (star.center(n+n))
    B -= 2

    while (A >= n/2) :
        B -= 2
        A += 1
        star = '*' * B
        print (star.center(n+n))
        if A == n :
            break

StarB (7)