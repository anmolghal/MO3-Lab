# Superclass for Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass for Automobile that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Function to create an Automobile instance and display the details
def main():
    # Set vehicle type to "car"
    vehicle_type = "car"
    
    # Collect information from the user
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an Automobile instance with the collected information
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Display the details in a readable format
    print("\nVehicle Details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")


# Run the main function
if __name__ == "__main__":
    main()
