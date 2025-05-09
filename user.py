class User:
   def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
   
users = []
def add_user(username: str, password: str):
    user = User(username, password)
    users.append(user)