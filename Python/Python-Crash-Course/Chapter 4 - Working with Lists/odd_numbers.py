# 4-6 Odd Numbers
odd_numbers = [value for value in range(1,20,2)]
for number in odd_numbers:
    print(number)

# 4-7 Multiple of 3
multiple_of_3 = [value for value in range(3,31,3)]
for number in multiple_of_3:
    print(number)

# 4-8 Number Cubed
number_cubed = []
for number in range(1,11):
    number_cubed.append(number**3)
for number in number_cubed:
    print(number)

# 4-9 Comprehension of Number Cubed
number_cubed_comprehension = [value**3 for value in range(1,11)]
print(number_cubed_comprehension)