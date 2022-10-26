import string
import random

def id_generator(size = 6, chars=string.ascii_uppercase + string.digits):
    shorten_URL = ''.join(random.choice(chars) for _ in range(size))
    return shorten_URL
