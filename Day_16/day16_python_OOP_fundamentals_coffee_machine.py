class CoffeeMachine:
    def __init__(self, brand, water_level):
        
        self.brand = brand
        self.water_level = water_level
        print(f"--- {self.brand} Coffee Machine is ready !")


    def make_coffee(self, cup_size):
        if self.water_level >= cup_size:
            self.water_level -= cup_size
            print(f"Here u are ur coffee... Enjoy ! (Remaining water:{self.water_level}ml)")
        else:
            print("Not enough water, buddy! Fill it again.")


my_machine = CoffeeMachine("Omath's Special", 500)


my_machine.make_coffee(150)
my_machine.make_coffee(200)
my_machine.make_coffee(200)

input("\n Press Power Button to exit...")
