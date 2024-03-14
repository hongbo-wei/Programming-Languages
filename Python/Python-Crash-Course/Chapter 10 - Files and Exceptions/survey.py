# 2nd Edition of Python Crash Course
# 10-5 Survey

file_name = 'survey.txt'

reason = ''
while True:
    fascination = input('Why do you like programming'
                        'or press enter to quit the program: ')
    if len(fascination) < 1:
        break

    reason += fascination + '\n'

with open(file_name, 'a') as file_object:
    file_object.write(reason)
