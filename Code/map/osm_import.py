from pyrosm import OSM
from pathlib import Path


class OSMImporter:
    def __init__(self, file_path: Path):
        self.osm_file = file_path
        self.osm = OSM(self.osm_file)

        self.road_network = self.osm.get_network(network_type="driving")

        self.nodes, self.edges = self.osm.get_network(
            nodes=True, network_type="driving"
        )

        self.graph = self.osm.to_graph(self.nodes, self.edges, simplify=True)

        print(self.osm)
        print(self.nodes)
        print(self.edges)
        print(self.graph)


osmimport = OSMImporter(
    "/home/dexter/Documents/GitHub/CarNavITSem2/Code/map/WEST.osm.pbf"
)
