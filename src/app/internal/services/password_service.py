import hashlib
import uuid


def get_hash_from_password(password: str) -> str:
    hash_salt = uuid.uuid4().hex
    result = hashlib.sha512(password.encode("utf-8") + hash_salt.encode("utf-8")).hexdigest()
    return result
