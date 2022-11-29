from parent import *

# Creating a child class ::
class SBI(Bank):
    def __init__(self):
        Bank.__init__(self)
        print("This is SBI bank rates 12.5% .")
    # Overriding show method of parent class ::
    def interest(self):
        print("Always greater than any other bank rates")




