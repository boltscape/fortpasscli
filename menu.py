import db_manager
from endecrypt import enpassword, depassword

def Menu():
    print("\n Menu \n")
    print("1. Create new password")
    print("2. Find password by site")
    print("3. Find password by email")
    print("4. Exit \n")
    c = int(input("Enter your choice: "))
    return c

def Create():
    site = input('Enter the name of the app/site: ')
    passw = enpassword(input('Enter password: '))
    mail = input("Enter email: ")
    username = input("Enter username (if applicable): ")
    if username == None:
        username = ''
    url = input("Enter the URL of the site: ")
    db_manager.add_pass(username, passw, mail, url, site)
    print("Added password successfully!")

def FindBySite():
    name = input("Enter name of the site/app you want the password for: ")
    db_res = db_manager.find_by_site(name)
    res = depassword(db_res)
    return res

def FindByMail():
    mail = input("Enter email address to search by: ")
    db_res = db_manager.find_by_mail(mail)
    res = depassword(db_res)
    return res