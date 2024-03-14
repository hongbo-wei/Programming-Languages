# 8-13

def build_profile(first, last, **user_info):
    """Build a dictionary containing all we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Hongbo', 'Wei', speciality='boxing',
                             skills='Computer Science', job='Software Engineer')
print(user_profile)