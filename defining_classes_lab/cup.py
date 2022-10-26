class Cup:
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity

    def fill(self,mililiters_to_add):
        if self.quantity + mililiters_to_add <=self.size:
            self.quantity = self.quantity + mililiters_to_add

    def status(self):
        return self.size-self.quantity

cup = Cup(100,50)
cup.fill(50)
cup.fill(10)
print(cup.status())