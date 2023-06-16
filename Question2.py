class vehicle :
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class car(vehicle):
    def seating_capacity(self,capacity):
        self.capacity = capacity
        return self.name_of_vehicle, capacity
    
b = car("tata",50,60)
print(b.seating_capacity(2))