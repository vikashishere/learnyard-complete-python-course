class Vehicle:
    def __init__(self):
        self.brand = 'brand-X'
        self.warranty = '10yrs'

    def description(self):
        return f"Vehicle: {self.brand} {self.model}"

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, model, doors):
        # super() calls the parent constructor
        super().__init__()
        self.model = model
        self.doors = doors

    # Override description method
    def description(self):
        return f"Car: {self.brand} <--> {self.model}, {self.doors}-door, {self.warranty}-warranty"

# --- Demo ---
print("\nExample 2: super() and Method Overriding")
car = Car("mini", 4)
print(car.description())