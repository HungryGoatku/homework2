# homework2
Small sha1 program that bruteforces the hashed guess into text and shows attempts taken 


# Requirements for Windows10
*Have latest installation of Python (3.7) within your machine
*You can do this within windows command line "python get-pip.py"

## Link example for MAC
[FOR MAC_USERS](https://docs.python-guide.org/starting/install3/osx/)

#RAWFILE of python file with comments
# We begin with importing the hashlib library for Python to generate secure hash message
import hashlib
# Receive hash input from user
shaOneHash = input("Please input the hash to crack. \n> ")

# We will open file full of random passwords
# hashed password Guess will be the password in plain text found within the file
# new_passwordList is new separate list within file that creates when checking for password

with open('10-million-password-list-top-1000000.txt') as passwordList:
    new_passwordList = [hashedpasswordGuess[:-1] for hashedpasswordGuess in passwordList]

    attempt = 0
    i = 0

# i represents variable to pass through new_passwordList,
    while i < len(new_passwordList):
        hashedpasswordGuess = new_passwordList[i]

# newGuess will take the hashed guess from list and compare it to user input by using SHA1
        newGuess = hashlib.sha1(bytes(hashedpasswordGuess, 'utf-8')).hexdigest()

# determine if user input hash is same to hash from file of passwords

# First condition will execute if they're is a match and show the attempts it took to find a match and terminate program
# Second condition will execute if they're isn't a match and show no match, following up with continued search for match

        if newGuess == shaOneHash:
            print(f'The password is {hashedpasswordGuess} which took {attempt} attempts.')
            exit(0)
        elif newGuess != shaOneHash:
            print(f'Password: {hashedpasswordGuess}, does not fit the match, trying next .. ')
            i += 1
            attempt += 1

# If there is absolutely no match found, this will execute and program terminates
print('Password could not be found with in textfile')

# Answers to questions
A. user input hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 ; password given: letmein ; attempts: 15
B. user input hash: 801cdea58224c921c21fd2b183ff28ffa910ce31 ; password given: vjhtrhsvdctcegth ; attempts: 999,967
