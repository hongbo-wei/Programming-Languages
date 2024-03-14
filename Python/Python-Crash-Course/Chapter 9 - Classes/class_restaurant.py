class Restaurant:
    """An attempt to simulate running restaurant"""

    def __init__(self,name, cuisine_type):
        """Initiate attribute 'name' and 'cuisine_type'"""
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print above two terms"""
        print(self.restaurant_name)
        print(self.cuisine_type,'\n')

    def open_restaurant(self):
        """Print a message that tells the restaurant is open"""
        print(f'The {self.restaurant_name} is open, come on in~\n')

    def set_number_served(self, times):
        self.number_served = times

    def increment_number_served(self, value):
        self.number_served += value

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'lemon', 'blueberry', 'cookie']
    def show(self, flavor):
        print(f'{self.restaurant_name} has {self.flavors[flavor]} ice cream')

# # exercise 9-1
# restaurant_practice = Restaurant('Lion','Wei')
# print(f'The restaurant is called {restaurant_practice.restaurant_name}')
# print(f'The cuisine type is {restaurant_practice.cuisine_type}')
# restaurant_practice.describe_restaurant()
# restaurant_practice.open_restaurant()
#
# # exercise 9-2
# restaurant_1 = Restaurant('Hot_Chicken', 'Chinese')
# restaurant_1.describe_restaurant()
#
# restaurant_2 = Restaurant('Pink_Blonde', 'British')
# restaurant_2.describe_restaurant()
#
# restaurant_3 = Restaurant('Pure_White', 'North European')
# restaurant_3.describe_restaurant()
#
# # exercise 9-4
# restaurant_4 = Restaurant('Lucky', 'Angel')
# restaurant_4.number_served = 10
# message = f'people have dined in the {restaurant_4.restaurant_name} restaurant'
# print(str(restaurant_4.number_served),message)
# restaurant_4.number_served = 55
# print(str(restaurant_4.number_served),message)
# restaurant_4.set_number_served(666)
# print(str(restaurant_4.number_served),message)
# for i in range(44):
#     restaurant_4.increment_number_served(i)
# print(f'{restaurant_4.restaurant_name} can serve up to {restaurant_4.number_served} people each day\n')
#
# # exercise 9-6 Ice Cream Stand 小店小摊
# ice_cream = IceCreamStand('Yummy', 'European')
# ice_cream.show(2)