from datetime import datetime, timedelta

from jose import jwt

# SECRET_KEY
# Algorithm
# Expiration Time

SECRET_KEY = "e5917a85a7e0d475812a6473dc585b4c6d5bcc6dc410d149eeac171b54b5e814"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_ecnode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_ecnode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_ecnode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
