from get_records import GetRecords

class ParsePartition(GetRecords):
    def __init__(self, query, path):
        GetRecords.__init__(self, query, path)
        self.records = self.get_records()

    def parse_partition(self):
        partitions = []
        for r in self.records:
            node = []
            node.append(r[2])
            node.append(r[3])
            node.append(r[4])
            partitions.append(node)
        return partitions

if __name__ == "__main__":
    parser = ParsePartition("Isocortex", "datasets/nature13186-s2.csv")
    print parser.parse_partition()
