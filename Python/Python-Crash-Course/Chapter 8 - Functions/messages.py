# 8-9 Messages
# 8-10 Sending Messages
# 8-11 Archived Messages

def show_messages(messages):
    """An example of using function dealing with a list"""
    print('The Content is in below: ')
    for message in messages:
        print(message)


def send_messages(unsent_messages, sent_messages):
    """Gradually empty a old list and create a new list"""
    while unsent_messages:
        sending = unsent_messages.pop()
        print(f'Sending message: {sending}')
        sent_messages.append(sending)


def archive_messages(unsent_messages, sent_messages):
    """An example of copy a input list, so the original one remain unchanged"""
    copy_messages = unsent_messages[:]

    while copy_messages:
        sending = copy_messages.pop()
        print(f'Sending message: {sending}')
        sent_messages.append(sending)


my_messages = ['Good day', 'Keep learning', 'Love yourself']
sent_message = []

# 8-9
show_messages(my_messages)

# 8-11 Optimized
print('')
archive_messages(my_messages, sent_message)
show_messages(my_messages)
show_messages(sent_message)
sent_message = []

# 8-11
print('')
send_messages(my_messages[:], sent_message)
show_messages(my_messages)
show_messages(sent_message)
sent_message = []

# 8-10
print('')
send_messages(my_messages, sent_message)
show_messages(my_messages)
show_messages(sent_message)