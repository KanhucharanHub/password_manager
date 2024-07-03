import hashlib
import pyotp

class AuthenticationManager:
    def __init__(self):
        self.master_password_hash = None

    def set_master_password(self, password: str):
        self.master_password_hash = hashlib.sha256(password.encode()).hexdigest()

    def verify_master_password(self, password: str) -> bool:
        return self.master_password_hash == hashlib.sha256(password.encode()).hexdigest()

class TwoFactorAuthenticationManager:
    def __init__(self):
        self.totp = pyotp.TOTP(pyotp.random_base32())

    def get_totp_uri(self, username):
        return self.totp.provisioning_uri(username, issuer_name="PasswordManagerApp")

    def verify_totp(self, token):
        return self.totp.verify(token)
