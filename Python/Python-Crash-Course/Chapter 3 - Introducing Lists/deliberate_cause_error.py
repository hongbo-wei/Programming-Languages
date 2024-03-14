cars = ['Lamborghini', 'Porsche']
print(len(cars))
i = len(cars)
# Out of index error: when printing last element, print(cars[len(cars)]), index should be len(cars)-1.
if i == len(cars):
    i = i - 1
    print(cars[i])