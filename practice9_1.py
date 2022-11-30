#创建一个restaurant的类
class Restaurant:
    '''第一次创建类'''
    def __init__(self,restaurant_name,cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (f"This restaurant was named {self.restaurant_name} and the type of cuisine is {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f"The {self.restaurant_name} is opening")

favourite_restaurant = Restaurant('ba yi lao ye','xin jiang cai')
print (f"my favourite restaurant is {favourite_restaurant.restaurant_name}")
print (f"my favourite restaurant'cuisine_type is {favourite_restaurant.cuisine_type}")
favourite_restaurant.describe_restaurant()
favourite_restaurant.open_restaurant()