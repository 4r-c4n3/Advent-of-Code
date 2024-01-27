import hashlib

pas = "bgvyzdsv"
for i in range(000000,999999) :
    digits = '{:d}'.format(i).zfill(4)
    check = pas + digits
    c_hash = hashlib.md5(check.encode())
    final = c_hash.hexdigest()
    if final[:5] == "00000":
        print(digits)