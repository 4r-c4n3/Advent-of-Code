def check(inp):
    strlen = len(inp) - 2
    linelen = len(inp)
    i = 0
    while i < len(inp) - 1:
        if inp[i:i + 2] == "\\x":
            strlen -= 3
            i += 4
        elif inp[i] == "\\":
            strlen -= 1
            i += 2
        elif inp[i] == " ":
            i += 1
        else:
            i += 1

    return linelen, strlen


real_length = string_len = 0
with open("2015_day8.txt") as file:
    for line in file.readlines():
        a, b = check(line.rstrip())
        real_length += a
        string_len += b

final = real_length - string_len
print(f"{real_length=} {string_len=}")
print(f"Final answer = {final}")
