n = int(input("Enter height: "))

for i in range(1, n+1):
    for j in range(0,i):
        print('*', end=" ")
    print("")

for i in range(1, n):
    for j in range(n,i,-1):
        print('*', end=" ")
    print("")
