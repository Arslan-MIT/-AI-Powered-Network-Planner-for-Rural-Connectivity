import pandas as pd
import folium
from sklearn.cluster import KMeans
import config

def cluster_network_nodes(dataset_path=config.CELL_TOWER_DATASET, num_clusters=config.NUM_CLUSTERS):
    # Load dataset
    data = pd.read_csv(dataset_path)
    data = data[['lat', 'lon']]  # Select required columns

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    data['cluster'] = kmeans.fit_predict(data)

    # Generate interactive map
    m = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=6)
    for _, row in data.iterrows():
        folium.Marker([row['lat'], row['lon']], popup=f"Cluster {row['cluster']}").add_to(m)

    m.save("dashboard/network_coverage_map.html")
    return "Network map generated successfully!"
