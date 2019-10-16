import hashlib

def encript(pwd):
    hashed = hashlib.sha512(str.encode(pwd))
    return hashed.hexdigest()

def procEncript(pwd):
     return encript(encript(pwd))

test = procEncript('test')
print((test),'test1')
test1 = procEncript('test')
print(test,'test2')
print(test == test1)
