from app.core.applications.auth.core.serializable import RequestLogin, TokenData
from app.core.applications.auth.core.QuerySet import GenericQuerySet
from app.core.applications.auth.core.exceptions import CredentialInvalid, InactiveUser
from app.core.applications.auth.core.models import Auth
from app.core.commons.enums.security import SecurityEnum
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext


class Oauth2Service:

    def __init__(self, data: RequestLogin):
        self.data_login = data
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self._pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> any:
        return self._pwd_context.hash(password)

    def authenticate(self):
        model_auth = GenericQuerySet(Auth)
        auth = model_auth.filter_one({'email': self.data_login.email})
        if not auth:
            raise CredentialInvalid()
        if not self.verify_password(self.data_login.password, auth.hashed_password):
            return False
        return auth

    def create_access_token(self) -> str:
        to_encode = {"sub": self.data_login.email}
        access_token_expires = timedelta(minutes=int(
            SecurityEnum.ACCESS_TOKEN_EXPIRE_MINUTES.value))
        expire = datetime.utcnow() + access_token_expires
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            SecurityEnum.SECRET_KEY.value,
            algorithm=SecurityEnum.ALGORITHM.value
        )
        return encoded_jwt

    @staticmethod
    def get_current_auth(token: str) -> Auth:
        try:
            payload = jwt.decode(
                token,
                SecurityEnum.SECRET_KEY.value,
                algorithms=[SecurityEnum.ALGORITHM.value]
            )
            username: str = payload.get("sub")
            if username is None:
                raise CredentialInvalid()
            token_data = TokenData(email=username)
        except JWTError as err:
            raise CredentialInvalid()
        model_auth = GenericQuerySet(Auth)
        auth = model_auth.filter_one({'email': token_data.email})

        if auth is None:
            raise CredentialInvalid()
        return auth

    @staticmethod
    async def get_current_active_auth(self, token: str):
        current_auth: Auth = self.get_current_auth
        if current_auth.disabled:
            raise InactiveUser()
        return current_auth
