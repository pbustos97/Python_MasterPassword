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

def userpunc(str):
    valid = False
    yes = ['yes','y','ye']
    no = ['no','n']
    while valid != True:
        punc = input(str)
        if punc.lower() in yes:
            check = input("Do the special characters have to be specific? (Y/N): ")
            if check in yes:
                characterList = []
                count = 0
                while True:
                    count += 1
                    character = input(count.__str__() + ". ")
                    characterList.append(character)
                    check = input('Are there more special characters?: ')
                    if check in yes:
                        pass
                    else:
                        break
                characterStr = ''.join(characterList)
                return characterStr
            else:
                return string.punctuation
        elif punc.lower() in no:
            return ''
        else:
            valid = False
