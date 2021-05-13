import datetime
from time import strptime

from algo import shortest_route
from hashtable import HashTable


class Package:
    def __init__(self, id, address, street, city, state, zip, deadline, mass, note):
        self.id = id
        self.address = address
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.status = 'At the hub'


# Function retrieves package from hash table and adds it to the inputted table
def load_package(package_list, truck, id):
    truck[id] = package_list[id]
    del package_list[id]


# Load packages that need to be delivered early
def sort_early_packages(package_table):
    early_packages = HashTable(20)
    for package in package_table:
        if (package.deadline == '10:30 AM' or
            package.deadline == '9:00 AM') and \
                package.note != 'Delayed on flight---will not arrive to depot until 9:05 am':
            load_package(package_table, early_packages, package.id)
    return early_packages


# Load packages that need to be on truck 2 and leave the hub after 9:05am
def sort_delayed_packages(package_table):
    delayed_packages = HashTable(20)
    for package in package_table:
        if package.note == 'Can only be on truck 2' or \
                package.note == 'Delayed on flight---will not arrive to depot until 9:05 am':
            load_package(package_table, delayed_packages, package.id)
    return delayed_packages


# Function uses shortest route to select remaining packages in order to fill the truck
# to its capacity of 16 packages
def fill_truck(packages, truck, graph, start):
    closest = 9999
    next_package = None

    while truck.num_elements < 16:

        for package in packages:
            current_distance = shortest_route(graph, start, package.address)
            if current_distance < closest:
                next_package = package
                closest = current_distance

        truck[next_package.id] = next_package
        start = next_package.address
        closest = 9999
        del packages[next_package.id]


# Function takes a list of packages and calculates the distance and time taken
# to deliver each package
def deliver_packages(truck, graph, start_time):
    time_input = strptime(start_time, '%H%M')
    distance = 0
    prev_destination = 'Hub'
    time = datetime.datetime(101, 1, 1, time_input.tm_hour, time_input.tm_min, time_input.tm_sec)
    for package in truck:
        leg_distance = shortest_route(graph, prev_destination, package.address)
        distance += leg_distance
        time = time + datetime.timedelta(hours=(leg_distance / 18))

        # print("Truck has travelled", round(distance, 2), "miles, and the time is",
        #    time.strftime("%H:%M:%S"))
        prev_destination = package.address
        package.status = "Delivered at: " + time.strftime("%H:%M:%S")

    # distance += shortest_route(graph, prev_destination, 'Hub')
    # print("Truck is back at the hub with a total distance of:", round(distance, 2))
    return distance


def deliver_packages_timed(truck, graph, start_time, end_time):
    time_input = strptime(start_time, '%H%M')
    time_end_input = strptime(end_time, '%H%M')
    distance = 0
    prev_destination = 'Hub'
    time = datetime.datetime(101, 1, 1, time_input.tm_hour, time_input.tm_min, time_input.tm_sec)
    time_end = datetime.datetime(101, 1, 1, time_end_input.tm_hour, time_end_input.tm_min, time_end_input.tm_sec)

    for package in truck:

        leg_distance = shortest_route(graph, prev_destination, package.address)
        distance += leg_distance
        time = time + datetime.timedelta(hours=(leg_distance / 18))
        if time >= time_end:
            return
        print("Truck has travelled", round(distance, 2), "miles, and the time is",
              time.strftime("%H:%M:%S"))
        prev_destination = package.address
        package.status = "Delivered at: " + time.strftime("%H:%M:%S")

    distance += shortest_route(graph, prev_destination, 'Hub')
    print("Truck is back at the hub with a total distance of:", round(distance, 2))
