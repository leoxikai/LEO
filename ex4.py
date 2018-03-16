cars=100
space_in_a_car=4
drives=30
passengers=90
cars_not_driven=cars-drives
cars_driven=drives
carpool_capacity=cars_driven*space_in_a_car
average_passenger_per_car=passengers/cars_driven


print(cars)
print(drives)
print(cars_not_driven)
print(carpool_capacity)
print(passengers)
print(average_passenger_per_car)