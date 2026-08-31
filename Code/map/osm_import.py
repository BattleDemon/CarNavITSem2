from pyrosm import OSM
from pathlib import Path


class OSMImporter:
    def __init__(self):
        # Finds the parent directory of this file (since the map is in the same dir)
        self.map_dir = Path(__file__).parent
        self.osm_file = self.map_dir / "weston_creek.osm.pbf"

        self.osm = OSM(self.osm_file)

        self.road_network = self.osm.get_network(network_type="driving")

        print("Columns")
        print(self.road_network.columns)

        print("Head")
        print(self.road_network.head())

        print("Length")
        print(len(self.road_network))


osmimport = OSMImporter()
