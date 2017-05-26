from allensdk.api.queries.mouse_connectivity_api import MouseConnectivityApi


class InspectCoordinates():
    """Get coordinates of acronym."""

    def __init__(self):
        """Construct a InspectCoordinates."""
        mca = MouseConnectivityApi()
        self.experiments = mca.experiment_source_search(
            injection_structures='root', transgenic_lines=0)

    def inspect_coordinates(self, query):
        """Inspect coordinates of query."""
        coordinates = [0, 0, 0]

        # get experiment data which relates to query
        exps = [exp for exp in self.experiments if exp['structure-abbrev'] == query]
        if len(exps) == 0:
            return False

        # take average over injection coordinates of the experiments
        for exp in exps:
            injection_coordinates = exp['injection-coordinates']
            for i, j in enumerate(injection_coordinates):
                coordinates[i] += j / len(exps)

        # insert query
        coordinates.insert(0, query)
        return coordinates


# test code
if __name__ == '__main__':
    query = u'ECT'
    inspector = InspectCoordinates()
    coordinate = inspector.inspect_coordinates(query)

    print coordinate
