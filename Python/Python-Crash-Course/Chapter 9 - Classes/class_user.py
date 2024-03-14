# exercise 9-3 User
class User:
    def __init__(self, first_name, last_name, age, gender, email, tel):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name +' ' + last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.tel = tel
        self.login_attempts = 0

    def describe_user(self):
        print(f'The user {self.full_name} is a {self.age}-year-old {self.gender}')
        print(f'contact this guy through {self.email} and tel: {self.tel}')

    def greet_user(self):
        if self.gender == 'male':
            print(f'Good day, handsome {self.first_name}\n')
        elif self.gender == 'female':
            print(f'Good day, pretty {self.first_name}\n')
        else:
            print('No such gender exists, goodbye\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# # exercise 9-7 Admin
# class Admin(User):
#     def __init__(self, first_name, last_name, age, gender, email, tel):
#         super().__init__(first_name, last_name, age, gender, email, tel)
#         self.privilege = Privileges()
#     # exercise 9-7 Admin
#     # def show_privileges(self):
#     #     privileges = ['can add post', 'can delete post', 'can ban user', 'can give credit to user']
#     #     for privilege in privileges:
#     #         print(f'Admin {privilege}')
#
# # exercise 9-8 Privileges
# class Privileges:
#     def show_privileges(self):
#         privileges = ['can add post', 'can delete post', 'can ban user', 'can give credit to user']
#         for privilege in privileges:
#             print(f'Admin {privilege}')


# # exercise 9-3
# user_wei = User('Hongbo', 'Wei', 19, 'male', 'hongbo_wei@king.com', '95666777')
# user_wei.describe_user()
# user_wei.greet_user()
#
# user_shen = User('Ruyi', 'Shen', 18, 'female', 'ruyi_shen@queen.com', '55888999')
# user_shen.describe_user()
# user_shen.greet_user()
#
# user_mysterious = User('Blonde', 'White', 18, 's', 'blonde_white@s.com', '00111222')
# user_mysterious.describe_user()
# user_mysterious.greet_user()
#
# # exercise 9-5 Login in attempts
# user_learning = User('Knowledge', 'Holy', 'before big bang', 'no gender', 'book', 'Internet')
# for i in range(4):
#     user_learning.increment_login_attempts()
#     print('Login attempts:',user_learning.login_attempts)
# user_learning.reset_login_attempts()
# print('Login attempts:', user_learning.login_attempts)
#
# # exercise 9-7 & 9-8
# admin_dragon = Admin('Light','Spirit', 'infinity','bisexual','sense','imagination')
# print('')
# # admin_dragon.show_privileges() for ex. 9-7
# admin_dragon.privilege.show_privileges()