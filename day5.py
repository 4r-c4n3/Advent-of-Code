repeat = vowel = bad_str = False
bad_strs = ["ab", "cd", "pq", "xy"]
vowels = ['a', 'e', 'i', 'o', 'u']
good_str = 0


def check_repeat(word):
    for i in range(0, len(word) - 1):
        if (i + 1) <= len(word):
            if word[i] == word[i + 1]:
                return True
    else:
        return False


def check_vowel(word):
    vol = 0
    for i in range(0, len(word) - 1):
        if (i + 1) < len(word):
            if word[i] in vowels:
                vol += 1
    if vol >= 3:
        return True
    else:
        return False


def check_bad_str(word):
    for i in range(0, len(word)):
        if (i + 2) <= len(word):
            if (word[i] + word[i + 1]) in bad_strs:
                return False
    else:
        return True


if __name__ == "__main__":
    with open("2015_day5.txt") as file:
        for line in file.readlines():
            i = check_repeat(line)
            j = check_vowel(line)
            k = check_bad_str(line)
            if i == j == k == True:
                good_str += 1
    print(good_str)
