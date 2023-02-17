
# ex 1

class Restaurant:

    def __init__(self,resturant_name,cuisine_type,):
        self.resturant_name = resturant_name
        self.cuisine_name = cuisine_type

    def describe_resturant(self):
        print(f"the resturant name is {self.resturant_name} and the cuisine type is {self.cuisine_name}")

    def open_resturant(self):
        print("the resturant is opend now !")


class IceCreamStand(Restaurant):

    def __init__(self, resturant_name, cuisine_type):
         super().__init__(resturant_name, cuisine_type)
         self.flavor = ["chocolate, vanilla, coffee"]

    def display_icecream_flavors(self):
        print(self.flavor)
        

my_icecream = IceCreamStand("Marble slab","sweets")
my_icecream.describe_resturant()
my_icecream.open_resturant()
my_icecream.display_icecream_flavors()
