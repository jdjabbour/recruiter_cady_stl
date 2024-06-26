

class Keeper():
    def __init__(self):
        self.username = None
        self.name = None
        self.auth_status = None

    def set_username(self, username):
        self.username = username

    def set_name(self, name):
        self.name = name

    def set_auth_status(self, auth_status):
        self.auth_status = auth_status