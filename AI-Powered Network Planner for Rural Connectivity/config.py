# 📍 OpenCellID API Key (Required for downloading full dataset)
OPENCELLID_API_KEY = "pk.ede0648db23d3859d638be221d11e876"

# 📍 Ookla Speedtest Data (Public AWS Open Dataset, No API Key Required)
OOKLA_API_URL = "https://registry.opendata.aws/speedtest-global-performance/"

# 📍 IODA (Internet Outage Data API, No API Key Required)
IODA_API_URL = "https://api.ioda.inetintel.cc.gatech.edu/v2/"

# 📍 Open Contracting Data API (Removed as it's unnecessary)
# OCDS_API_URL = "https://data.open-contracting.org/api/"
# OCDS_API_KEY = "your_api_key_here"

# 📂 Dataset Paths
CELL_TOWER_DATASET = "data/opencellid_sample.csv"
OSM_BUILDING_DATA = "data/osm_buildings.geojson"
POPULATION_DENSITY_DATA = "data/global_human_settlement.csv"

# 📍 Default Clustering Parameters
NUM_CLUSTERS = 5

# 📍 IODA Default Parameters (Modify dynamically in scripts)
DEFAULT_COUNTRY = "US"  # Change as needed
DEFAULT_TIME_SPAN = "7d"  # Last 7 days of outage data
