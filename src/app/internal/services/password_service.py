import hashlib
import uuid


def get_hash_from_password(password: str) -> str:
    # hash_salt =
    hash_salt = ""
    return hashlib.sha512(password + hash_salt).hexdigest()
