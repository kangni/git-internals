import os
import hashlib


GIT_DIR = ".git_demo"


def init():
    os.mkdir(GIT_DIR)

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f"{GIT_DIR}/objects/{oid}", "wb") as out:
        out.write(data)
    return oid

def get_object(oid):
    with open(f"{GIT_DIR}/objects/{oid}", "rb") as f:
        return f.read()