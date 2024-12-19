area = 0
final = 0
dimensions = []
slack = 0
with open("2015_day2.txt") as file:
    for i in file:
        dimensions = i.split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        area = 2 * l * w + 2 * w * h + 2 * h * l
        dimensions.sort()
        slack = (l * w * h) / max(l, w, h)
        final += area + slack

    print(f"final area : " + str(final))
