import random
import string
from get_state import state
from seed import seed
from userinput import userinput, usersize, userpunc

def generate(size, seed, state, punc):
#state called to make sure generated password doesn't change if reentered
    seed
    state
    if punc == True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(size))
    else:
        password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size))
    print (password)

def finished():
    finished = userpunc("Are you finished? ")
    if finished == True:
        exit()
        return True
    if finished == False:
        usize = usersize()
        uinput = userinput(usize)
        upunc = userpunc("Use puncuations? (Y/N): ")

        generate(usize, seed(uinput), state(), upunc)
        return False

cont = False

while cont != True:
    cont = finished()
