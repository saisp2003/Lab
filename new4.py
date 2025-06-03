#change the model of the car using getter and  setter
class Car:
    def __init__(self,brand, model,year):
        self.__model = model
        self.__brand = brand
        self.__year = year
    def get_brand(self):
        return self.__brand
    def get_year(self):
        return self.__year    

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model
    def set_brand(self, brand):
        self._brand=brand
    def set_year(self, year):
        self.__year = year
car = Car("Toyota","innova","2023")
print(car.get_model())
print(car.get_brand())
print(car.get_year())    
car.set_model("fortuner")
car.set_year("2024")
print(car.get_model())

































































