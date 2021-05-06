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
def load_early_packages(package_table):
    early_packages = HashTable(20)
    for package in package_table:
        if package.deadline == '10:30 AM' or package.deadline == '9:00 AM':
            load_package(package_table, early_packages, package.id)
    return early_packages


# Load packages that need to be on truck 2 and leave the hub after 9:05am
def load_delayed_packages(package_table):
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
