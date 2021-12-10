import time
from base64 import b64decode, b64encode

numbs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


k = input("encrypt or decrypt:   ")

if k == "encrypt":
    j = input("enter your password:   ")

    tst = time.process_time()

    f = open(f'{j}.txt', 'wb')

    jfk = b64encode(j.encode("utf-8"))

    for i in range(len(numbs)):
        jfk = b64encode(jfk)

    print("writing... ")

    f.write(jfk)
    print(f'time taken {time.process_time() - tst} sec')
    print("done")
    f.close()
elif k == "decrypt":
    j = input("enter file name - the .txt")

    tst = time.process_time()

    f = open(f'{j}.txt', 'rb')

    c = f.read()

    jfk = b64decode(c)

    for i in range(len(numbs)):
        jfk = b64decode(jfk)
    
    jfk = jfk.decode("utf-8")

    print("done.")
    print()
    print(f'time taken {time.process_time() - tst}')
    print()
    print(f'your decypted password is: {jfk}')

    f.close()





