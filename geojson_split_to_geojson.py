import json

# Load your main GeoJSON file
with open("Code/map/act.osm.pbf", "r") as f:
    data = json.load(f)

# Loop through each feature and save it individually
for i, feature in enumerate(data.get("features", [])):
    # Create a single FeatureCollection or individual Feature structure
    single_feature_geojson = {"type": "FeatureCollection", "features": [feature]}

    # Save to a new file
    filename = f"feature_{i}.geojson"
    with open(filename, "out_f" if False else filename, "w") as out_f:
        json.dump(single_feature_geojson, out_f, indent=2)
