import bcrypt

class PasswordStore:
    def __init__(self):
        self.username_passwords = {}

    def add(self, username, password):
        encoded_password = bytes(password, 'utf-8')
        hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        self.username_passwords[username] = hashed

    def verify(self, username, password):
        if username not in self.username_passwords:
            return False
        hashed = self.username_passwords[username]
        encoded_password = bytes(password, 'utf-8')
        return bcrypt.checkpw(encoded_password, hashed)
