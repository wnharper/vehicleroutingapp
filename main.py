import datetime
from algo import *
from data import *
from package import *

# Load packages into hash table from CSV file
all_packages = load_package_data('package_file.csv')

# Load distance data into dict from CSV file
distance_graph = load_distance_data('distance_table.csv')

# Packages that need to be delivered by before 10:30am
early_packages = load_early_packages(all_packages)

# Packages that need to be on truck 2 and leave the hub after 9:05am
delayed_packages = load_delayed_packages(all_packages)

# fill truck 1 up with packages closest to package 13
fill_truck(all_packages, early_packages, distance_graph, early_packages['15'].address)

# fill truck 2 up with packages closest to package 3
fill_truck(all_packages, delayed_packages, distance_graph, delayed_packages['36'].address)

# Order packages using greedy algorithm + Dijkstra's
truck_1 = calculate_route(early_packages, distance_graph, "Hub")
truck_2 = calculate_route(delayed_packages, distance_graph, "Hub")
truck_3 = calculate_route(all_packages, distance_graph, "Hub")

t1_distance = 0
prev_destination = 'Hub'
truck1_time = datetime.datetime(101, 1, 1, 8, 0, 0)
for package in truck_1:
    leg_distance = shortest_route(distance_graph, prev_destination, package.address)
    t1_distance += leg_distance
    truck1_time = truck1_time + datetime.timedelta(hours=(leg_distance / 18))
    print("Truck 1 has travelled", round(t1_distance, 2), "miles, and the time is", truck1_time.strftime("%H:%M:%S"))
    prev_destination = package.address
    package.status = "Delivered at: " + truck1_time.strftime("%H:%M:%S")

t1_distance += shortest_route(distance_graph, prev_destination, 'Hub')
print("Truck 1 is back at the hub with a total distance of:", round(t1_distance, 2))
print("")

for package in truck_3:
    leg_distance = shortest_route(distance_graph, prev_destination, package.address)
    t1_distance += leg_distance
    truck1_time = truck1_time + datetime.timedelta(hours=(leg_distance / 18))
    print("Truck 1 has travelled", round(t1_distance, 2), "miles, and the time is", truck1_time.strftime("%H:%M:%S"))
    prev_destination = package.address
    package.status = "Delivered at: " + truck1_time.strftime("%H:%M:%S")

t1_distance += shortest_route(distance_graph, prev_destination, 'Hub')
print("Truck 1 is back at the hub with a total distance of:", round(t1_distance, 2))
print("")

truck2_time = datetime.datetime(101, 1, 1, 9, 5, 0)
t2_distance = 0
for package in truck_2:
    leg_distance = shortest_route(distance_graph, prev_destination, package.address)
    t2_distance += leg_distance
    truck2_time = truck2_time + datetime.timedelta(hours=(leg_distance / 18))
    print("Truck 2 has travelled", round(t2_distance, 2), "miles, and the time is", truck2_time.strftime("%H:%M:%S"))
    prev_destination = package.address
    package.status = "Delivered at: " + truck2_time.strftime("%H:%M:%S")

t2_distance += shortest_route(distance_graph, prev_destination, 'Hub')
print("Truck 2 is back at the hub with a total distance of:", round(t2_distance, 2))
print("")

print("Total distance travelled today:", round(t1_distance + t2_distance, 2))

for package in truck_1:
    print("Package ID:", package.id, package.address, package.status)
