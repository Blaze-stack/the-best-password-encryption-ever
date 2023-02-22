import time
from base64 import b64decode, b64encode

numb = 36


k = input("encrypt or decrypt:   ")

if k == "encrypt":
    j = input("enter your password:   ")

    tst = time.process_time()

    f = open(f'{j}.blaze', 'wb')

    jfk = b64encode(j.encode("utf-8"))

    for i in range(numbs):
        jfk = b64encode(jfk)

    print("writing... ")

    f.write(jfk)
    print(f'time taken {time.process_time() - tst} sec')
    print("done")
    f.close()
elif k == "decrypt":
    j = input("enter file name - the .blaze part:   ")

    tst = time.process_time()

    f = open(f'{j}.blaze', 'rb')

    c = f.read()

    jfk = b64decode(c)

    for i in range(numbs):
        jfk = b64decode(jfk)
    
    jfk = jfk.decode("utf-8")

    print("done.")
    print()
    print(f'time taken {time.process_time() - tst}')
    print()
    print(f'your decypted password is: {jfk} sec')

    f.close()





