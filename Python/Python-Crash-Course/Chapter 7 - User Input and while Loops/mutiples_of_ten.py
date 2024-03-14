# Multiples of Ten

prompt = 'Enter an integer, and I will tell you whether it is a'
prompt += 'multiple of ten: '

number = input(prompt)

if int(number) % 10 == 0:
    print('It is a multiple of 10')
else:
    print('It is NOT a multiple of 10')
