# assignment 2 (password generator)

import string
import random

print(" Hello, welcome to the password generator!")

length = int(input("Enter password length :"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
special = string.punctuation

all = lower + upper + num + special
pass1 = random.sample(all,length)

password = "".join(pass1)

print(password)


