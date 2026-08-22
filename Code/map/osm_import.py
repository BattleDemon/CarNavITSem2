from pyrosm import OSM


class OSMImporter:
    def __init__(self):
        self.osm_file = "act.osm.pbf"
        self.osm = OSM(self.osm_file)

        self.road_network = self.osm.get_network(network_type="driving")

        print(self.roads)
