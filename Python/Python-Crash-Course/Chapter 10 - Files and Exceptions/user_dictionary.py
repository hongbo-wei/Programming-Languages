# 10-13 User Dictionary

import json
from pathlib import Path


def get_stored_userinfo(path):
    """Get stored user information if available"""
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None


def get_new_userinfo(path):
    """Prompt for new user information"""
    user_name = input('What is your name: ')
    user_dream = input('What is the dream you want the worst: ')
    user_info = {'name': user_name,
                 'dream': user_dream,
                 }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by his/her information"""
    path = Path('user_info.json')
    user_info = get_stored_userinfo(path)
    if user_info:
        print(f"Welcome back, {user_info['name']}! "
              f"I hope all the best for you to pursuit your dream "
              f"'{user_info['dream']}'")
    else:
        user_info = get_new_userinfo(path)
        print(f"We'll keep your secret, come back anytime, {user_info['name']}!")


greet_user()
