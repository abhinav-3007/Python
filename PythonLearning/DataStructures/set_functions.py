s = set(map(int, input().split()))
num = int(input())
print(s)
for i in range(0, num):
    com = input().split()
    if com[0] == "pop":
        s.pop()
    elif com[0] == "remove":
        s.remove(int(com[1]))
    elif com[0] == "discard":
        s.discard(int(com[1]))
    print(s)
print(sum(s))
