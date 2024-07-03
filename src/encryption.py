from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)
    
    @staticmethod
    def generate_key() -> bytes:
        return Fernet.generate_key()

    def encrypt(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data: str) -> str:
        return self.cipher.decrypt(data.encode()).decode()
