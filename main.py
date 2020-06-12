import math
X = int(input("Enter the number: "))

#Step 1
Y = math.floor(X/10**9) #Number of iterations to be perfomed

while(Y > 0):
#Step 2
    Z = math.floor(X/10**8) #Second most significant digit of X

#Step 3
    if X < 5 * (10**9):
        X = X + 5 * (10**9)

#Step 4
    X = math.floor(((X*X)/10**5)%(10**10))

#Step 5
    X = (1001001001 * X)%(10**10)

#Step 6
    if X < 10**8:
        X = X + 9814055677
    else:
        X = (10**10) - X
    
#Step 7
    X = (10**5)*(X%(10**5)) + math.floor(X/10**5)

#Step 8
    X = (1001001001 * X)%(10**10)

#Step 9
    a = ""
    for i in str(X):
        if int(i) > 0:
            a = a + str(int(i) - 1)
        else:
            a = a + str(int(i))
    X = int(a)

#Step 10
    if X < 10**5:
        X = X*X + 99999
    else:
        X = X - 99999
    
#Step 11
    if X > 0:
        while(X < 10**9):
            X = 10*X

#Step 12
    X = (math.floor(X*(X - 1)/(10**5)))%(10**10)
    
#Step 13
    Y = Y - 1
    
print("Randomized number is ->", X)

    












