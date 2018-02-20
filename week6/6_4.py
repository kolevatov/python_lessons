#   Гражданская оборона
townCount = int(input())
towns = list(map(int, input().split()))
shelterCount = int(input())
shelters = list(map(int, input().split()))

cnt = 0
for i in towns:
    towns[cnt] = (i, cnt)
    cnt += 1
towns.sort()

cnt = 0
for i in shelters:
    shelters[cnt] = (i, cnt+1)
    cnt += 1
shelters.sort()

minPos = 0
result = []
for i in range(townCount):
    result.append('')

for i in towns:
    min = 10000000000
    pos = minPos
    while pos < shelterCount:
        diff = abs(shelters[pos][0] - i[0])
        if diff < min:
            min = diff
            minPos = pos
        elif diff >= min:
            break
        pos += 1
    result[i[1]] = shelters[minPos][1]

print(*result)
