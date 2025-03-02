from models.network_planning import cluster_network_nodes
from utils.cost_estimation import estimate_cost
from utils.fetch_network_data import fetch_speedtest_data

# Step 1: Generate network plan
print(cluster_network_nodes())

# Step 2: Estimate cost
cost = estimate_cost(5, 100)
print(f"Estimated Cost: ${cost}")

# Step 3: Fetch speed test data
print(fetch_speedtest_data())
