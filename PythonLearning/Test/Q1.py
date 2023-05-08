N = int(input("Enter the number of processes: "))
co = input("Enter the calling order: ").split()
io = input("Enter the ideal order: ").split()
time = 0
while len(co)>0:
    if co[0] == io[0]:
        co.pop(0)
        io.pop(0)
        time += 1
    else:
        co.append(co.pop(0))
        time += 1

print(time)
