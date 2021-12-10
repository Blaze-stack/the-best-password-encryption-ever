from base64 import b64decode, b64encode

numbs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


k = input("encrypt or decrypt:   ")

if k == "encrypt":
    j = input("enter your password:   ")

    f = open(f'{j}.txt', 'wb')

    jfk = b64encode(j.encode("utf-8"))

    for i in range(len(numbs)):
        jfk = b64encode(jfk)

    print("writing... ")

    f.write(jfk)
    print("done")
    f.close()
elif k == "decrypt":
    j = input("enter file name - the .txt")

    f = open(f'{j}.txt', 'rb')

    c = f.read()

    jfk = b64decode(c.decode("utf-8"))

    for i in range(len(numbs)):
        jfk = b64decode(jfk)

    
    print(jfk)

    f.close()





