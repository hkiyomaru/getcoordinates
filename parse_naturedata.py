import pandas as pd


class ParseNatureData(object):
    """Parse Acronym from `nature13186-s2.xlsx (sheet 2)`."""

    def __init__(self, path):
        """Construct a ParseNatureData."""
        self.records = pd.read_table(path, sep=',')

    def get_acronym(self):
        """Get Acronym."""
        partitions = self.records['Acronym']

        return partitions


if __name__ == "__main__":
    acr_parser = ParseNatureData("datasets/nature13186-s2.csv")
    acronym = acr_parser.get_acronym()

    print acronym
