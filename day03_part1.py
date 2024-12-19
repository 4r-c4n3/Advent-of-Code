x = y = 0
visited = []
file = open("2015_day3.txt")
line = file.readline()
for i in line:
    if i == '^':
        x += 1
    elif i == 'v':
        x -= 1
    elif i == '>':
        y += 1
    elif i == '<':
        y -= 1
    else:
        continue
    address = str(x) + "," + str(y)
    if address not in visited:
        visited.append(address)
    else:
        continue
print(f"{len(visited) + 1}")
