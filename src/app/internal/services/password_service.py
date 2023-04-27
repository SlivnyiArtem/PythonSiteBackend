import hashlib
import uuid


def get_hash_from_password(password: str) -> str:
    # hash_salt =
    # hash_salt = ""
    result = hashlib.sha512(password.encode("utf-8")).hexdigest()
    # result = hashlib.sha512(password.encode('utf-8'))
    # raise Exception(result)
    return result
