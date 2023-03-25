# Explore Hashlib to encrypt text:
import hashlib

email = 'jkr@gmail.com'
pwd = 'ChairOnTableWith3Legs'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_mail = 'jkr@gmail.com'
your_password = 'ChairOnTableWith3Legs'

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()
if email == your_mail and pwd_hash == hashed_your_password:
    print('Right user')
else:
    print('Wrong user')

#__________________________________________________________
hacker_email = 'jkr@gmail.com'
hacker_password = '2329e22c9a4de221abeabaf22b72c7fc'
#if I use hacker password then it will give Wrong password
#__________________________________________________________

print(pwd)
print(pwd_hash)