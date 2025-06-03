#Create a sublcass electric car and override the start method

class Vehicle :
    def __start__engine(self):
        pass
class car(Vehicle):
    total_count=0
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.yaer=year
        self.is__running=False
        car.total_count += 1

    def get_model(self):
        return self.model
    def set_model(self,new_value):
        self.model=new_value
    def start_engine(self):
        self.is__running=True
        print(f"{self.model}Engine started")

class ElectricCar(car):
    def start_engine(self):
        if not self.is__running:
            self.is__running = True
            print(f"{self.model} electric engine started silently.")
        else:
            print(f"{self.model} electric engine is already running.")
            

my_car=car("Toyota","Innova",2020)
my_car.start_engine()
my_car.set_model("Fortuner")
my_car.start_engine()
my_electric_car = ElectricCar("Tesla", "Cybertruck", 2024)
my_electric_car.start_engine()
print(f"Total cars created: {car.total_count}")









            

