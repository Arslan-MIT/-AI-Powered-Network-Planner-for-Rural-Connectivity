import streamlit as st
from utils.cost_estimation import estimate_cost
from utils.fetch_network_data import fetch_speedtest_data
import models.network_planning as planner

st.title("AI-Powered Network Planner")

# Generate Network Map
if st.button("Generate Network Plan"):
    result = planner.cluster_network_nodes()
    st.write(result)

# Cost Estimation
num_towers = st.number_input("Enter number of towers", min_value=1, value=3)
fiber_length = st.number_input("Enter fiber length (km)", min_value=1, value=50)
cost = estimate_cost(num_towers, fiber_length)
st.write(f"Estimated Deployment Cost: ${cost}")

# Internet Performance Data
if st.button("Fetch Speed Test Data"):
    speedtest_data = fetch_speedtest_data()
    st.write(speedtest_data)
