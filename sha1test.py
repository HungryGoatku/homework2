import hashlib

shaOne = input("Please input the hash to crack. \n> ")

with open('10-million-password-list-top-1000000.txt') as passwordList:
    new_passwordList = [hashedpasswordGuess[:-1] for hashedpasswordGuess in passwordList]

    attempt = 0
    i = 0

    while i < len(new_passwordList):
        hashedpasswordGuess = new_passwordList[i]

        newGuess = hashlib.sha1(bytes(hashedpasswordGuess, 'utf-8')).hexdigest()

        if newGuess == shaOne:
            print(f'The password is {hashedpasswordGuess} which took {attempt} attempts.')
            exit(0)
        elif newGuess != shaOne:
            print(f'Password: {hashedpasswordGuess}, does not fit the match, trying next .. ')
            i += 1
            attempt += 1

print('Password could not be found with in textfile')
