class Vehicle:
    def __init__(self, vehicle_type):   # initiate vehicle type
        self.type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof): # initiate automobile details
        super().__init__('Automobile')  # call parent constructor
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.roof = roof

# Main program
__main__ = "__main__"
car = Vehicle(input("Enter the vehicle type: "))    # get vehicle type from user
year = input("Enter the vehicle year: ")    # get vehicle year from user
make = input("Enter the vehicle make: ")    # get vehicle make from user
model = input("Enter the vehicle model: ")  # get vehicle model from user
doors = input("Enter the number of doors(2 or 4): ")    # get number of doors from user
roof = input("Enter the type of roof(solid or sun roof): ")  # get roof type from user
auto = Automobile(year, make, model, doors, roof)   # create Automobile object

# Display vehicle information
print(f"Vehicle Type: {car.type}")
print(f"Year: {auto.year}")
print(f"Make: {auto.make}")
print(f"Model: {auto.model}")
print(f"Doors: {auto.doors}")
print(f"Roof: {auto.roof}")