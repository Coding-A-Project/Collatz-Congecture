n = eval(input('Enter Number To Check Collatz Conjecture: '))
count = 0
if (n == 1):
    count = 0
    print("Sorry, this is an infinite loop of 1 - 2 - 4 - 2 - 1 - 4. And it's aldready 1.")
    print("Count =", count)
elif(n == 2):
    count = 2
    print("Sorry, this is an infinite loop of 1 - 2 - 4 - 2 - 1 - 4.")
    print("Count =",count)
elif(n == 4):
    count = 2
    print("Sorry, this is an infinite loop of 1 - 2 - 4 - 2 - 1 - 4")
    print("Count =",count)
while(n != 1):
    if(n % 2 == 0):
        count = count + 1
        n = (n/2)
        print(n)
    else:
        count = count + 1
        n = (3*n)+1
        print(n)
print("Count =",count)