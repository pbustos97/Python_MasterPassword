import string

def userinput(size):
    print('!!! Username and password are case-sensitive !!!')
    print('Service has to be exact, not shortened or lengthened. It can be different cases')
    username = input("Username: ")
    password = input("Master Password: ")
    service = input("Service: ")
    return str(username + password + service.lower() + size.__str__())

def usersize():
    size = input("Password Size: ")
    valid = None
    while valid != True:
        if size.isdigit():
            valid = True
            return int(size)
        else:
            valid = False
            size = input("Password Size: ")

def userpunc(string):
    valid = None
    yes = ['yes','y','ye']
    no = ['no','n']
    while valid != True:
        punc = input(string)
        if punc.lower() in yes:
            valid = True
            return True
        elif punc.lower() in no:
            valid = True
            return False
        else:
            valid = False
