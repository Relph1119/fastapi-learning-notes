from secrets import compare_digest

from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from models.data.sqlalchemy_models import Login
from passlib.context import CryptContext

# 设置加密编码
crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

http_basic = HTTPBasic()


def get_password_hash(password):
    return crypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(credentials: HTTPBasicCredentials, account: Login):
    try:
        # 比较凭证
        is_username = compare_digest(credentials.username, account.username)
        is_password = compare_digest(credentials.password, account.username)
        verified_password = verify_password(credentials.password, account.passphrase)
        return verified_password and is_username and is_password
    except Exception as e:
        print(e)
        return False
