import bcrypt 

def hash_pass(password : str) -> str:
    sal = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"),sal)
    return hashed.decode("utf-8")


def verify_password(password : str , hash_pass: str)->bool:
    return bcrypt.checkpw(password.encode("utf-8"),hash_pass.encode("utf-8"))