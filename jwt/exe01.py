import jwt

key = 'test'

payload = {
    'id_user': 1,
    'life_token': 3600
}

token = jwt.encode(payload, key, algorithm='HS256')
print(token)

result = jwt.decode(token, key, verify=True, algorithm='HS256')

print(result)
