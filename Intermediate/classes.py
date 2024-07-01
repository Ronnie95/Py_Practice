class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username




user_1 = User("002", "Ronnie")
# user_1.id = "002"
# user_1.username = "Ron"
print(user_1.username)