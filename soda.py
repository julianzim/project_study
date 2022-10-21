class Soda:
    def __init__(self, add=None):
        self.add = add
    
    def show_my_drink(self):
        if self.add == None:
            print('Soda')
        else:
            print('Soda and', self.add)

myDrink = Soda('lime')
myDrink.show_my_drink()