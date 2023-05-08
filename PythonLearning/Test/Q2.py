N = int(input("Enter number of people: "))
li = input('Enter the heights: ').split()
count = 1
for i in range(1,N):
    if li[i-1] > li[i]:
        count += 1

print(count)
