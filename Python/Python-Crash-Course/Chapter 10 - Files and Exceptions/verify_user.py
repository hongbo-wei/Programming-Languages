# 10-14 Verify User: modify remember_me.py from book, adding verification process

import json
from pathlib import Path


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path, *username):
    """Prompt for new user information"""
    # If arbitrary argument is input, then it means:
    # The current username doesn't match the last username.
    # Note: arbitrary argument creates a tuple, so we have to convert the type
    if username:
        username = username[0]
        contents = json.dumps(username)
        path.write_text(contents)
    else:
        username = input('What user name you would like to use: ')
        contents = json.dumps(username)
        path.write_text(contents)
    return username


def greet_user():
    """Greet the user by his/her information"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}! ")

    # if there is no username stored, prompt for username.
    else:
        username = get_new_username(path)
        print(f"We'll remember you when come back, {username}!")


def verify_user(path):
    """Verify if the current user is the last user, if not, update username."""
    current_user = input('Enter username for verification: ')
    if current_user == get_stored_username(path):
        greet_user()
    else:
        print('Not last user, updating information initiating.')
        new_username = get_new_username(path, current_user)
        print(f"I'll greet you next time, {new_username}")


def storing_data_game(path):
    """Run the whole data storing game"""
    if path.exists():
        verify_user(path)
    else:
        greet_user()


path = Path('username.json')
storing_data_game(path)
