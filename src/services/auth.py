from passlib.context import CryptContext

class AuthService:
    def __init__(self) -> None:

        self.pwd_context = CryptContext(schemes=["bcrypt"], depreacted="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password):
        return self.pwd_context.has(password)