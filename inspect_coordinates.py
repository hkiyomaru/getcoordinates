from allensdk.api.queries.mouse_connectivity_api import MouseConnectivityApi

class InspectCoordinates():
    def __init__(self):
        mca = MouseConnectivityApi()
        self.experiments = mca.experiment_source_search(injection_structures='root', transgenic_lines=0)

    def inspect_coordinate(self, query):
        coordinate = [0, 0, 0]
        exps = [exp for exp in self.experiments if exp['structure-abbrev'] == query]
        for exp in exps:
            for i in range(len(coordinate)):
                coordinate[i] += exp['injection-coordinates'][i]
        for i in range(len(coordinate)):
            coordinate[i] /= len(exps)
        return coordinate
            

# test code
if __name__ == '__main__':
    query = u'ECT'
    ic = InspectCoordinates()
    coordinate = ic.inspect_coordinate(query)
    print coordinate

