from hashtable import HashTable
from package import Package
import csv

# Create hashtable and load packages into table from CSV file
# package_table = HashTable(5)
# package_dictionary = {}
# with open('package_file.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)  # skip first line (headers) of csv file
#     for line in csv_reader:
#         package_table[line[0]] = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
#         package_dictionary[line[0]] = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
#
# print(package_table['14'].address)

graph = {}



graph_test = {'A': {'B': 3, 'C': 6},
              'B': {'A': 3, 'C': 4},
              'C': {'A': 6, 'B': 4}}

with open('distance_table.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_headings = next(csv_reader)

    headings_arr = []
    for heading in csv_headings:
        headings_arr.append(heading)

    for heading in headings_arr:
        graph[heading] = {}

    for index, line in enumerate(csv_reader):
        for i, digit in enumerate(range(2, len(line))):
            if line[0] != headings_arr[i]:
                graph[line[0]][headings_arr[i]] = float(line[i+2])

   # print(headings_arr)

        # graph[line[0]] = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])


print(graph)

print(graph['Housing Auth. of Salt Lake County'])

if graph == graph_test:
    print("True")
