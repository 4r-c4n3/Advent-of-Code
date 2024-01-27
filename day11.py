def check_abc(inp):
    for i in range(0, len(inp) - 2):
        if inp[i + 1] == chr(ord(inp[i]) + 1) and inp[i + 2] == chr(ord(inp[i]) + 2):
            return True
    else:
        return False


def check_2aa(inp):
    count = i = 0
    while i < (len(inp) - 1):
        if inp[i] == inp[i + 1]:
            count = count + 1
            i = i + 2
        i = i + 1
    if count >= 2:
        return True
    else:
        return False


def check_iol(inp):
    for i in range(0, len(inp)):
        if inp[i] == 'i' or inp[i] == 'o' or inp[i] == 'l':
            return False
    else:
        return True


def increment(inp):
    chars = list(inp)
    for i in range(len(chars) - 1, -1, -1):
        if chars[i] != 'z':
            chars[i] = chr(ord(chars[i]) + 1)
            break
        else:
            chars[i] = 'a'

    return ''.join(chars)


if __name__ == "__main__":

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w']
    old_pass = 'hepxxyzz'

    while True:
        new = increment(old_pass)
        if check_iol(new) and check_abc(new) and check_2aa(new):
            print(new)

            break
        old_pass = new
