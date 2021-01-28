import os

import argon2
import menu
from argon2 import PasswordHasher

ph = PasswordHasher(hash_len=24)

print("Welcome to Fortpass.")
secret = "$argon2id$v=19$m=102400,t=2,p=8$QBKvEdJkTdr9oS4EIh7tJQ$0P3eRYJPKr5qaIPG5t2OVQEOY98E/VKD"
def app():
    pw = input("Enter your password: ")
    try:
        if ph.verify(secret,pw):
            c = menu.Menu()
            while True:
                if c == 1:
                    menu.Create()
                    c = menu.Menu()
                elif c == 2:
                    result = menu.FindBySite()
                    for rec in result:
                        print("Site: ", rec[3])
                        print("Username: ", rec[0])
                        print("E-mail: ", rec[1])
                        print("Password: ",rec[2], "\n")
                    c = menu.Menu()
                elif c == 3:
                    result = menu.FindByMail()
                    for rec in result:
                        print("E-mail: ", rec[1])
                        print("Username: ", rec[0])
                        print("Site: ", rec[3])
                        print("Password: ",rec[2], "\n")
                    c = menu.Menu()
                else:
                    print("Goodbye!")
                    break
    except argon2.exceptions.VerifyMismatchError:
        print("Oops, wrong password! Try again: ")
        app()

app()