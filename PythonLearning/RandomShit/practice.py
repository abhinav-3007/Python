size = int(input())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))
taken = 0
taken_value = 0
values_kg = []
for i in range(len(weights)):
    values_kg.append(values[i]/weights[i])

last_w = 0
last_v = 0
last_vk = 0

while size >= taken and len(values_kg) != 0:
    valuable = max(values_kg)
    ind = values_kg.index(valuable)
    values_kg.remove(valuable)
    values_kg.insert(ind,0)
    taken_value+=values[ind]
    taken+=weights[ind]
    last_w = weights[ind]
    last_v = values[ind]
    last_vk = valuable

taken-=last_w
taken_value-=last_v
rem = size-taken
taken_value+=(last_vk*rem)

print(round(taken_value))
