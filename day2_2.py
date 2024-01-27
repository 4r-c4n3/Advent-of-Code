total = 0
dimensions = []

with open("2015_day2.txt") as file:
    print(" " + "_" * 60 + " ")
    print(f"| length |  width  | height | perimeter_ribbon | area ribbon |  ")
    print("|"+"_" * 60 + "|")
    for i in file:
        dimensions = i.split('x')
        dimensions.sort()
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        perimeter_ribbon = l + l + w + w + h + h - max(l, w, h) - max(l, w, h)
        area_ribbon = l * w * h
        total += perimeter_ribbon + area_ribbon
        print(f'| {l: ^ 5}  |  {w: ^ 5}  |  {h: ^ 5} |  {perimeter_ribbon: ^ 14}  |  {area_ribbon: ^ 10} |')

    print("|"+"_" * 60 + "|")
    print(f"total ribbon :  {str(total)=} ")