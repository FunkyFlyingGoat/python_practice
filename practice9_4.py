#在餐厅类中增加就餐人数的属性
class Restaurant:
    '''第一次创建类'''
    def __init__(self,restaurant_name,cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = '0'

    def set_number_served(self,numbers):
        self.number_served = numbers
    
    def number_reading(self):
        print (f"There are {self.number_served} peopel in the restaurant")

    def describe_restaurant(self):
        print (f"This restaurant was named {self.restaurant_name} and the type of cuisine is {self.cuisine_type}")
    
    def open_restaurant(self):
        print (f"The {self.restaurant_name} is opening")

favourite_restaurant = Restaurant('ba yi lao ye','xin jiang cai')
favourite_restaurant.describe_restaurant()
favourite_restaurant.open_restaurant()
favourite_restaurant.number_reading()
favourite_restaurant.set_number_served(10)
favourite_restaurant.number_reading()