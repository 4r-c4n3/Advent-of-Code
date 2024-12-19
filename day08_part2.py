def make_string(inp):
    new_len = len(inp) + 1
    old_len = len(inp)
    i = 0
    while i < len(inp):
        if inp[i] == "\\":
            new_len = new_len + 1
            i = i + 1
            print("\\")
        elif inp[i] == " ":
            i = i + 1
            print(inp[i])
        elif inp[i] == "\"":
            new_len = new_len + 1
            i = i + 1
            print("\"")
        else:
            i = i + 1

    return new_len, old_len - 1


new = old = 0
real_length = string_len = 0
with open("2015_day8.txt") as file:
    for line in file.readlines():
        a, b = make_string(line)
        new += a
        old += b

final = new - old
print(f"{new=} {old=}")
print(f"Final answer = {final}")
