from hashlib import pbkdf2_hmac
import secrets

#generates a random salt for password hashing
def generate_salt():
    return secrets.token_bytes(64)

#password hashing function using PBKDF2
def hash_password(password, salt):
    hashed_password = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password

#password verification function
def verify_password(stored_password_hash, provided_password, salt):
    hashed_provided_password = hash_password(provided_password, salt)
    return secrets.compare_digest(stored_password_hash, hashed_provided_password)