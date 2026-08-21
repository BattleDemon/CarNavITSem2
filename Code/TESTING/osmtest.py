import pyrosm

# Get filepath to test PBF dataset
fp = pyrosm.get_data("test_pbf")
print("Filepath to test data:", fp)


# Initialize the OSM parser object
osm = pyrosm.OSM(fp)

# See the type
print("Type of 'osm' instance: ", type(osm))

# Read all drivable roads
# =======================
drive_net = osm.get_network(network_type="driving")
drive_net.plot()
print("end")
