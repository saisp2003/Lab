#create a class vehicle and create a method to start the engine use encapsulation and use parent class and child class
class Vehicle:
    def __init__(self, make, model):
        self._make = make            # Protected attribute
        self._model = model          # Protected attribute
        self._engine_started = False # Private attribute

    def start_engine(self):
        self._engine_started = True
        print(f"{self._make} {self._model} engine started.")

    def is_engine_started(self):
        return self._engine_started

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors

    def start_engine(self):
        super().start_engine()
        print("Car is ready to drive.")

# Example usage:
car = Car("Toyota", "Corolla", 4)
car.start_engine()
print("Engine started?", car.is_engine_started())
