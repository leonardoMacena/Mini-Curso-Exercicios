import jwt

priva = open("id_rsa", 'r')
payload = {
    'id_user': 1,
    'life_token': 3600
}

keystring_priva = priva.read()
priva.close()
token = jwt.encode(payload, keystring_priva, algorithm='RS256')

pub = open("id_rsa.pub", 'r')
keystring_pub = pub.read()
pub.close()
payload = jwt.decode(token, keystring_pub,  verify=True)
print(payload)
