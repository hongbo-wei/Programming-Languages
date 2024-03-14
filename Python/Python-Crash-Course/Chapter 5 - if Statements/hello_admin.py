# 5-8 Hello Admin
# 5-9 No Users

user_list = ['Admin', 'Hongbo', 'Champ', 'Dragon', 'Bruce']

user_list = []

if user_list:
    for i in user_list:
        if i == 'Admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print(f'Hello {i}, thank you for logging in again')

else:
    print('We need to find some users')
