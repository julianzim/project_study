class Soda:
    def __init__(self, add=None):
        if isinstance(add, str):
            self.add = add
        else:
            self.add = None
    
    def show_my_drink(self):
        if self.add:
            print(f'Soda and {self.add}')
        else:
            print('Soda')

myDrink1 = Soda()
myDrink2 = Soda('lime')
myDrink3 = Soda(123)
myDrink4 = Soda('lime, mint')
myDrink1.show_my_drink()
myDrink2.show_my_drink()
myDrink3.show_my_drink()
myDrink4.show_my_drink()