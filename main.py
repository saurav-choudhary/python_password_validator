import re

password = input('Enter a password to check:\n')

if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print('Yay! you have a secure password!')
else:
    print('Your password needs your attention!')