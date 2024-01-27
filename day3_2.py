santa_x = santa_y = 0
robo_x = robo_y = 0
santa_visited = ['0,0']
robo_visited = []

file = open("2015_day3.txt")
line = file.readline()
santa = line[::2]
robo = line[1::2]

for i in santa:
    if i == '^':
        santa_x += 1
    elif i == 'v':
        santa_x -= 1
    elif i == '>':
        santa_y += 1
    elif i == '<':
        santa_y -= 1
    else:
        continue
    s_address = str(santa_x) + "," + str(santa_y)
    if s_address not in santa_visited:
        santa_visited.append(s_address)
    else:
        continue

for i in robo:
    if i == '^':
        robo_x += 1
    elif i == 'v':
        robo_x -= 1
    elif i == '>':
        robo_y += 1
    elif i == '<':
        robo_y -= 1
    else:
        continue
    r_address = str(robo_x) + "," + str(robo_y)
    if r_address not in robo_visited and r_address not in santa_visited:
        robo_visited.append(r_address)
    else:
        continue
s_house = len(santa_visited)
r_house = len(robo_visited)
print(f"santa visited = {s_house} and robo santa visited ={r_house} ")
print(f"total house visited = {s_house + r_house}")
