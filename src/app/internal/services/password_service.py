import hashlib
import uuid


def get_hash_from_password(password: str) -> str:
    hash_salt = uuid.uuid4().hex
    return hashlib.sha512(password + hash_salt).hexdigest()
