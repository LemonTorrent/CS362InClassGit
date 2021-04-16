import random

def genPassword(n):
    password = ""
    for i in range(n):
        randChar = random.randrange(48, 126)
        password = password + chr(randChar)

    print("Generated password:", password)

n = 12
genPassword(n)
