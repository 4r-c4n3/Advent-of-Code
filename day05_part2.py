import hashlib

pas = "bgvyzdsv"
for i in range(0, 9999999):
    check = pas + str(i)
    c_hash = hashlib.md5(check.encode())
    final = c_hash.hexdigest()
    if final[:6] == "000000":
        print(f"we got hash {final} at concatenated value {i} ")
