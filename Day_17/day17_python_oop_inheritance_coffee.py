class CoffeeMachine:
    def __init__(self, brand, water_level):
        self.brand = brand
        self .water_level = water_level
        print(f"--- {self.brand} Coffee Machine is READY !---")

class PremiumMachine(CoffeeMachine): 
    def __init__(self, brand, water_level, milk_level):
       
        super().__init__(brand, water_level)
        self.milk_level = milk_level
    
    
    def make_coffee(self, cup_size):
        if self.water_level >= cup_size:
            self . water_level -= cup_size
            print(f"\nMade A Normal Coffee... (Reamainning Water: {self.water_level}ml) ")

        else:
            print("Water are not enough !")

    def make_latte(self, milk_needed):
        if self.milk_level >= milk_needed:
            self.milk_level -= milk_needed
            print(f"Latte is ready ! (remainning milk: {self.milk_level}ml)")

        else:
            print("Milk Are Not Enough !")

my_pro_machine = PremiumMachine("Omath's Pro", 1000, 500)

my_pro_machine.make_coffee(200)
my_pro_machine.make_latte(150)

input("\nPress Powerkey to exit...")
