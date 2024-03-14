from employee import Employee

first = input('Enter your first name: ')
last = input('Enter your last name: ')
salary = input('Enter your current annual salary in numbers only: ')

bruce = Employee(first, last, salary)
bruce.show_salary()

print('You got promoted!')
bruce.give_raise()
bruce.show_salary()