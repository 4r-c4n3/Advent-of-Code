import re


def check(inp):
    result = ""
    pattern = re.compile(r"((\d)\2*)")
    matches = pattern.finditer(inp)

    for match in matches:
        length = len(match.group(1))
        result += str(length) + match.group(2)

    return result


a = "3113322113"
for _ in range(0, 50):
    b = check(a)
    a = b

print(len(b))
