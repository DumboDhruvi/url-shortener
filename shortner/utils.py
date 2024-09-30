from random import *
from string import *
# chars you want in your string
chars = ascii_lowercase + ascii_uppercase + digits

def gen(l: int) -> str:
    word = []
    for i in range(l):
        word.append(choice(chars))
        
    return "".join(word)
    