class ParkingLot:
    def __init__(self):
        self.level_a = [None] * 20  # Level A parking spots
        self.level_b = [None] * 20  # Level B parking spots

    def assign_parking_spot(self, vehicle_number):
        # Check if there is an available spot in Level A
        for i in range(20):
            if self.level_a[i] is None:
                self.level_a[i] = vehicle_number
                return {"level": "A", "spot": i + 1}
        
        # If Level A is full, check Level B
        for i in range(20):
            if self.level_b[i] is None:
                self.level_b[i] = vehicle_number
                return {"level": "B", "spot": i + 21}
        
        return "Parking is full."

    def retrieve_parking_spot(self, vehicle_number):
        for i in range(20):
            if self.level_a[i] == vehicle_number:
                return {"level": "A", "spot": i + 1}
            elif self.level_b[i] == vehicle_number:
                return {"level": "B", "spot": i + 21}
        return "Vehicle not found."

if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("Parking Lot Tracker")
        print("1. Assign a parking spot")
        print("2. Retrieve parking spot number")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(f"Assigned spot: {result}")

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(f"Retrieved spot: {result}")

        elif choice == "3":
            break
