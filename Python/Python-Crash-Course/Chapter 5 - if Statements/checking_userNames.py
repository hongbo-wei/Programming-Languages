# 5-10 Checking Usernames

current_users = ['Admin', 'Hongbo', 'Champ', 'Dragon', 'Bruce']

lower_users = [item.lower() for item in current_users]
print(lower_users)

new_users = ['Atom', 'Lewis', 'Champ', 'Pycharm', 'Bruce']

for new_user in new_users:
    if new_user.lower() in lower_users:
        print(f'The username {new_user} has bee taken, '
              f'please enter a new username')
    else:
        print(f'This username {new_user} is available')
