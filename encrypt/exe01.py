import bcrypt

print(dir(bcrypt))

def crypt(pwd):
    return bcrypt.hashpw(str.encode(pwd), bcrypt.gensalt())

text = open('senha', 'w')
senhas =  crypt('test')
print(dir(senhas))
text.write(senhas.decode())
text.close()
text2 = open('senha', 'r')
senha =  text2.read()
print(type(senha))
print(bcrypt.checkpw( str.encode('test'), str.encode(senha)))
