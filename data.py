from hashtable import HashTable
import csv
from package import Package


# Create hashtable and load packages into table from CSV file
def load_package_data(file):
    all_packages = HashTable(5)
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip first line (headers) of csv file
        for line in csv_reader:
            all_packages[line[0]] = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                            line[8])
        return all_packages


def load_distance_data(file):
    # Load distance table csv into dictionary
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_headings = next(csv_reader)

        # Create list with table headings
        headings_arr = []
        for heading in csv_headings:
            headings_arr.append(heading)

        # Initialize graph dictionary
        graph = {}
        for heading in headings_arr:
            graph[heading] = {}

        # Populate graph dictionary with data from csv
        for index, line in enumerate(csv_reader):
            for i, digit in enumerate(range(2, len(line))):
                if line[0] != headings_arr[i]:
                    graph[line[0]][headings_arr[i]] = float(line[i + 2])
        return graph
