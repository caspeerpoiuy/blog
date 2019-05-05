import hashlib


def md5_user_id(id):
    hash = hashlib.md5()
    hash.update(bytes(id))
    return hash.hexdigest()