from passlib.context import CryptContext
from db import sqlTranslate

class pwd(object):
    """description of class"""

    pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
    )

    def encrypt_password(password):
        return pwd.pwd_context.encrypt(password)

    def check_encrypted_password(password, hashed):
        return pwd.pwd_context.verify(password, hashed)
    
    def check_password_for_user(user: str, password: str):
        return pwd.check_encrypted_password(password, sqlTranslate.sqlTranslate().read_user_hash(user))

    def store_new_user(name: str, password: str):
        sqlTranslate.sqlTranslate().add_user(name, pwd.encrypt_password(password))