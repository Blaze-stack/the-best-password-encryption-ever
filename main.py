from base64 import b64decode, b64encode

numbs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

j = input("enter your password:   ")

f = open(f'{j}.txt', 'wb')

jfk = b64encode(j.encode("utf-8"))

for i in range(len(numbs)):
    jfk = b64encode(jfk)

print("writing... ")

f.write(jfk)
print("done")
f.close()