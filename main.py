#####################################
#                                   #
#       Warren Harper - C950        #
#       Student ID: 001326657       #
#                                   #
#####################################

from algo import *
from data import *
from package import *

# Load packages into hash table from CSV file
all_packages = load_package_data('package_file.csv')

# Load distance data into dict from CSV file
distance_graph = load_distance_data('distance_table.csv')

# Packages that need to be delivered by before 10:30am
early_packages = sort_early_packages(all_packages)

# Packages that need to be on truck 2 and leave the hub after 9:05am
delayed_packages = sort_delayed_packages(all_packages)

# fill truck 1 up with packages closest to package 13
fill_truck(all_packages, early_packages, distance_graph, early_packages['13'].address)

# fill truck 2 up with packages closest to package 3
fill_truck(all_packages, delayed_packages, distance_graph, delayed_packages['3'].address)

# Order packages using greedy algorithm + Dijkstra's
truck_1 = calculate_route(early_packages, distance_graph)
truck_2 = calculate_route(delayed_packages, distance_graph)
truck_3 = calculate_route(all_packages, distance_graph)

# Command line interface to view package deliveries
# User instructions
print("Enter '1' to see all packages delivered, '2' to enter a time")

user_input = input("Enter 1 or 2: ")

if user_input == "1":
    dist1 = deliver_packages(truck_1, distance_graph, '0800')
    dist2 = deliver_packages(truck_2, distance_graph, '0905')
    dist3 = deliver_packages(truck_3, distance_graph, '0945')

    # Print out the status of each package
    print("Truck 1:")
    for package in truck_1:
        print("Package ID:", package.id, package.address, package.status)
    print("\nTruck 2:")
    for package in truck_2:
        print("Package ID:", package.id, package.address, package.status)
    print("\nTruck 3:")
    for package in truck_3:
        print("Package ID:", package.id, package.address, package.status)

    print("\nTotal distance traveled today:", round(dist1 + dist2 + dist3, 2), "miles.\n")

elif user_input == "2":
    print("Enter a time after 9am in military time eg. 0935 ")
    user_input = input("Enter a time: ")
    timed_dist1 = deliver_packages_timed(truck_1, distance_graph, '0800', user_input)
    timed_dist2 = deliver_packages_timed(truck_2, distance_graph, '0905', user_input)
    timed_dist3 = deliver_packages_timed(truck_3, distance_graph, '0945', user_input)
    total_distance = timed_dist1 + timed_dist2 + timed_dist3

    # Print out the status of each package
    print("Truck 1:")
    for package in truck_1:
        print("Package ID:", package.id, package.address, package.status)
    print("\nTruck 2:")
    for package in truck_2:
        print("Package ID:", package.id, package.address, package.status)
    print("\nTruck 3:")
    for package in truck_3:
        print("Package ID:", package.id, package.address, package.status)

    print("\nTotal distance traveled today:", round(total_distance, 2), "miles.\n")



