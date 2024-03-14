# 7-2 Restaurant Seating

prompt = 'Enter how many people are in your dinner group: '

seat_judgement = input(prompt)
if int(seat_judgement) <= 8:
    print("You table is ready, come on in~")
else:
    print("I'm sorry that you have to wait for a big table")