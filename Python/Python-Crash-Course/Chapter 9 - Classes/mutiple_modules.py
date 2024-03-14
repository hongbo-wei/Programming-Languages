# exercise 9-12 Multiple Modules
from class_user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, email, tel):
        super().__init__(first_name, last_name, age, gender, email, tel)
        self.privilege = Privileges()

class Privileges:
    def show_privileges(self):
        privileges = ['can add post', 'can delete post', 'can ban user', 'can give credit to user']
        for privilege in privileges:
            print(f'Admin {privilege}')