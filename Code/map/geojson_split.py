import json

# Load your multi-subsection GeoJSON
with open("Data/ACTGOV_DISTRICTS_-2248938068983619392.geojson", "r") as f:
    geojson_data = json.load(f)

extracts = []

# Loop through each feature to create an extract definition
for index, feature in enumerate(geojson_data["features"]):
    # Use a property name (like 'name' or 'id') for the filename, fallback to index
    properties = feature.get("properties", {})
    name = (
        properties.get("DISTRICT_NAME", f"subsection_{index}").replace(" ", "_").lower()
    )

    extracts.append(
        {
            "output": f"{name}.osm.pbf",
            "description": f"Extract for {name}",
            "multipolygon": feature["geometry"],
        }
    )

# Save to Osmium configuration format
osmium_config = {"extracts": extracts}

with open("extract_config.json", "w") as f:
    json.dump(osmium_config, f, indent=4)

print("Osmium extract configuration created successfully!")
