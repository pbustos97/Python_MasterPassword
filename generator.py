import random
import string
from get_state import state
from seed import seed
from userinput import userinput, usersize, userpunc

stringStr = string.ascii_letters + string.digits
yes = ['yes','ye','y']
no = ['no','n']

def generate(size, seed, state, punc):
#state called to make sure generated password doesn't change if reentered
    seed
    state
    password = ''.join(random.choice(stringStr + punc) for x in range(size))
    print (password)

def finished():
    finished = input("Are you finished? ")
    if finished in yes:
        exit()
        return True
    if finished in no:
        usize = usersize()
        uinput = userinput(usize)

        generate(usize, seed(uinput), state(), userpunc("Use puncuations? (Y/N):"))
        return False
    else:
        return False

cont = False

while cont != True:
    cont = finished()
