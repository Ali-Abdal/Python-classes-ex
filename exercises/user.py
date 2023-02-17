
class User():

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def get_user_info(self):
        print(f"""
        username: {self.username}
        email: {self.email}
        password: {self.password}
        """)

    def greet_user(self):
        print(f"Greetings {self.username}!")

class Privilges:

    def __init__(self,privileges = ["kick","ban","delete"]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"admins can {self.privileges}")

class Admin(User):

    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.privileges = Privilges()
    
abdal = Admin("Abdal","Abdal@example.com","12345")

abdal.get_user_info()
abdal.privileges.show_privileges()
abdal.greet_user()

