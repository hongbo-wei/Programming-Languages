# exercise 9-14 lottery
from random import choice

my_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e')
ls = list()
for i in range(4):
    ls.append(choice(my_tuple))
print(ls)
# use ** join ** method to convert list to string
secret = ''.join([str(elem.upper()) for elem in ls])
print(f'As long as you have {secret} on your ticket, you win the lottery')

# exercise 9-15 Analysis of lottery
my_ticket = ['e', '5', '2', '0']
count = 0

while my_ticket != ls:
    ls = list()
    for i in range(4):
        ls.append(choice(my_tuple))
    count += 1
print(ls)
print(f'Keep buying a ticket with same characters, it takes {count} times participating to win the lottery')
