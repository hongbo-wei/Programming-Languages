# 5-11 Ordinal Numbers

numbers = list(range(1,10)) # Create a list using list() and range() functions.
print(numbers)

for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')
