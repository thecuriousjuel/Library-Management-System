from pwinput import pwinput

try:
    p = pwinput(prompt='Your favorite flower? ', mask='x')
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)