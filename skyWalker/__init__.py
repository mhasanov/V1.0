from db import sqlTranslate
from hash import pwd

def login():
    un = input("Enter user name: ")
    pw = input("Enter user password: ")
    pwd.pwd.check_encrypted_password(pw , sqlTranslate.sqlTranslate().read_user_hash(un)[0][0])

