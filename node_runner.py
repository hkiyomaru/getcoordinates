from parse_naturedata import ParseNatureData
from inspect_coordinates import InspectCoordinates
import argparse
import csv

argparser = argparse.ArgumentParser()
argparser.add_argument('--dataset', action='store', dest='path',
                       default="datasets/nature13186-s2.csv")
args = argparser.parse_args()

write_dir = "coordinates/"


def get_coordinates(inspector, acronym):
    """Get coordinates of given acronym."""
    coordinates = []
    for query in acronym:
        result = inspector.inspect_coordinates(query)
        if result:
            coordinates.append(result)
        else:
            print "Cannot get coordinates of " + query

    return coordinates


def write_csv(coordinates, write_path):
    """Dump a csv file."""
    writer = csv.writer(open(write_path, "wb"))

    for c in coordinates:
        appendList = list(c)
        writer.writerow(appendList)

    print "Writing csv-file has been completed."


if __name__ == '__main__':
    dataset_path = args.path
    write_path = write_dir + "coordinates.csv"

    dataset_parser = ParseNatureData(dataset_path)
    acronym = dataset_parser.get_acronym()

    inspector = InspectCoordinates()
    coordinates = get_coordinates(inspector, acronym)

    write_csv(coordinates, write_path)
