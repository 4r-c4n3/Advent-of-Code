rows = 999
clos = 999
array = [[0 * i] * 999 for i in range(999)]
with open("2015_day6.txt") as file:
    for line in file.readlines():
        block = line.split()
        if block[0] == "toggle":
            x1, y1 = block[1].split(",")
            x2, y2 = block[3].split(",")
            for i in range(int(x1), int(x2)):
                for j in range(int(y2), int(y2)):
                    if array[i][j] == 1:
                        array[i][j] = 0
                    else:
                        array[i][j] = 1
        elif block[0] == "turn on":
            x1, y1 = block[2].split(",")
            x2, y2 = block[4].split(",")
            for i in range(int(x1), int(x2)):
                for j in range(int(y1), int(y2)):
                    array[i][j] = 1

        elif block[0] == "turn off":
            x1, y1 = block[2].split(",")
            x2, y2 = block[4].split(",")
            for i in range(int(x1), int(x2)):
                for j in range(int(y1), int(y2)):
                    array[i][j] = 0

print(array)