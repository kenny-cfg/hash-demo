class PasswordStore:
    def __init__(self):
        self.username_passwords = {}

    def add(self, username, password):
        self.username_passwords[username] = password

    def verify(self, username, password):
        return username in self.username_passwords and self.username_passwords[username] == password
