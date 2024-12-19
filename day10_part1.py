def check(inp):
    i = 0
    join = ""
    while i < len(inp):
        if i <= len(inp) - 3 and inp[i] == inp[i + 1] == inp[i + 2]:
            join += '3' + inp[i]
            i += 3
        if i <= len(inp) - 3 and inp[i] == inp[i + 1] == inp[i + 2]:
            join += '3' + inp[i]
            i += 3
        elif i <= len(inp) - 2 and inp[i] == inp[i + 1]:
            join += '2' + inp[i]
            i += 2
        else:
            join += '1' + inp[i]
            i += 1
    return join


a = "3113322113"
for _ in range(0, 40):
    b = check(a)
    a = b

print(len(b))
