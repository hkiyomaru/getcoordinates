from parse_partition import ParsePartition
from inspect_coordinates import InspectCoordinates
import argparse
import csv

write_dir = "coordinates/"

def get_coordinates(query_list):
    coordinates = []
    inspector = InspectCoordinates()
    for p in partitions:
        try:
            coordinate = inspector.inspect_coordinate(p)
            coordinates.append(coordinate)
        except:
            print "Cannot get the coordinate of " + p
    return coordinates

def write_csv(coordinates, write_path):
    writer = csv.writer(open(write_path, "ab"))
    for c in coordinates:
        appendList = list(c)
        writer.writerow(appendList)
    print "Writing CSV is a success."

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-query', action='store',dest='query',default='Isocortex')
    argparser.add_argument('-path', action='store', dest='path', default="datasets/nature13186-s2.csv")
    query = argparser.parse_args().query
    dataset_path = argparser.parse_args().path
    write_path = write_dir + query + ".csv"

    dataset_parser = ParsePartition(query, dataset_path) 
    partitions = dataset_parser.parse_partition()
    
    coordinates = get_coordinates(partitions)
    write_csv(coordinates, write_path)
