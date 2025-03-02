# AI-Powered Network Planner for Rural Connectivity

## 📌 Overview
This project, **AI-Powered Network Planner for Rural Connectivity**, leverages AI, geospatial data, and network analysis to optimize the placement of telecom towers in underserved rural areas. It integrates multiple datasets to identify the best locations for network expansion while considering cost, population density, and existing infrastructure.

## 🚀 Features
- **📡 Cell Tower Placement Optimization**: Uses K-Means clustering to determine the best locations for telecom towers.
- **📊 Internet Outage Analysis**: Integrates IODA API to analyze regional network outages.
- **📍 Geospatial Data Integration**: Processes OSM and OpenCellID data for real-world tower placement.
- **📈 Population-Based Network Planning**: Incorporates GHSL population density data for accurate demand forecasting.
- **🖥️ Interactive Dashboard**: Provides a user-friendly Streamlit interface for visualizing network expansion plans.

## 📁 Project Structure
```
📂 ai_network_planner/
│── 📂 data/                          # Store datasets (e.g., OpenCellID, OSM, GHSL, etc.)
│── 📂 models/                        # AI & ML models (e.g., K-Means clustering)
│    │── network_planning.py          # AI logic for tower placement
│── 📂 utils/                         # Helper functions
│    │── cost_estimation.py           # Cost estimation logic
│    │── fetch_network_data.py        # Internet speed & outage data retrieval
│── 📂 dashboard/                     # Streamlit-based UI
│    │── app.py                        # Main Streamlit UI file
│── main.py                           # Central execution file
│── requirements.txt                   # Dependencies
│── config.py                         # Configuration file (API keys, dataset paths)
│── README.md                         # Project Documentation
│── .gitignore                         # Ignore unnecessary files
```

## 🔑 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai_network_planner.git
   cd ai_network_planner
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set API Keys & Configurations**
   - Open `config.py` and replace placeholder API keys with your actual credentials.
   - Example:
     ```python
     OPENCELLID_API_KEY = "your_api_key_here"
     IODA_API_KEY = "your_api_key_here"
     ```

## 🔧 Usage
### Run the Main Application
```bash
python main.py
```
### Start the Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```

## 📊 Data Sources
- **[OpenCellID](https://opencellid.org/)** (Cell Tower Locations)
- **[OpenStreetMap](https://www.openstreetmap.org/)** (Geospatial Building Data)
- **[IODA](https://ioda.inetintel.cc.gatech.edu/)** (Internet Outage Data)
- **[GHSL](https://ghsl.jrc.ec.europa.eu/)** (Population Density Data)

## 🤖 AI Models Used
- **K-Means Clustering**: For optimal network tower placement.
- **Geospatial Analysis**: To integrate multiple datasets for better decision-making.

## 🚀 Future Enhancements
- Integration with real-time network performance APIs.
- Support for additional geospatial analysis methods.
- Cost-effectiveness analysis with financial models.

## 🛠 Contributors
- **Muhammad Arslan** (Lead Developer)

## 📜 License
This project is licensed under the MIT License.

## ⭐ Support
If you find this project useful, please ⭐ the repository and share your feedback!

