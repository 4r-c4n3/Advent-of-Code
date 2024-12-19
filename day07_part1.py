def do_not(arg1, arg2):
    arg2 = ~arg1
    return arg2


def do_signal(arg1, arg2):
    arg2 = arg1
    return arg2


def do_and(arg1, arg2, arg3):
    arg3 = arg1 & arg2
    return arg3


def do_or(arg1, arg2, arg3):
    arg3 = arg1 | arg2
    return arg3


def do_lshift(arg1, arg2, arg3):
    arg3 = arg1 >> int(arg2)
    return arg3


def do_rshift(arg1, arg2, arg3):
    arg3 = arg1 << int(arg2)
    return arg3


with open("2015_day7.txt") as file:
    for line in file.readlines():
        block = line.split(" ")
        if block[0] == "NOT":
            do_not(block[1], block[3])
        elif block[1] == "AND":
            do_and(block[0], block[2], block[4])
        elif block[1] == "NOT":
            do_and(block[0], block[2], block[4])
        elif block[1] == "NOT":
            do_and(block[0], block[2], block[4])
        elif block[1] == "NOT":
            do_and(block[0], block[2], block[4])
        else:
            do_signal(block[0], block[2])
