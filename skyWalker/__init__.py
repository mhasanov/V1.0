from db import sqlTranslate
from hash import pwd

def dothis():
    pwd.pwd.store_new_user("John", "John")
    un = input("Enter user name")
    pw = input("Enter user password")
    print(pwd.pwd.check_encrypted_password(pw , sqlTranslate.sqlTranslate.read_user_hash(un)[0][0]))

dothis()