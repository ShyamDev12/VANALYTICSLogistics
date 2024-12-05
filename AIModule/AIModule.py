import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Application Title
st.title("VAnalytics: AI-powered Logistics Management System 🚛")

# Section 1: Sidebar Inputs for Real-Time Scenario Simulation
st.sidebar.header("Logistics Input Parameters")
st.sidebar.write("Configure inputs for route optimization and utilization analytics.")

# Dynamic Inputs
start_location = st.sidebar.text_input("Start Location", "Warehouse A")
destination = st.sidebar.text_input("Destination", "Client B")
delivery_urgency = st.sidebar.selectbox("Delivery Urgency", ["Low", "Medium", "High"])
traffic_conditions = st.sidebar.slider("Traffic Conditions (0: Clear - 10: Heavy)", 0, 10, 5)
fuel_cost_per_liter = st.sidebar.number_input("Fuel Cost (per liter in INR)", min_value=50, max_value=150, value=100)
maintenance_status = st.sidebar.selectbox("Truck Maintenance Status", ["Up-to-Date", "Due Soon", "Critical"])
days_in_operation = st.sidebar.slider("Days in Operation", 1, 100, 50)

# Section 2: Route Optimization
st.header("🚚 AI-Driven Route Optimization")
st.write("Optimize the delivery route to minimize fuel usage and travel time based on input parameters.")

if st.button("Run Route Optimization"):
    # Simulated optimization result
    optimized_route = f"Route optimized for {start_location} → {destination} with {traffic_conditions}/10 traffic conditions."
    estimated_time = round(np.random.uniform(2, 8), 2)
    fuel_estimate = round(np.random.uniform(50, 120), 2)

    st.success(optimized_route)
    st.metric(label="Estimated Travel Time (hrs)", value=f"{estimated_time} hrs")
    st.metric(label="Estimated Fuel Usage (liters)", value=f"{fuel_estimate} L")

# Section 3: Predictive Analytics
st.header("📊 Predictive Analytics for Truck Utilization")
st.write("Analyze truck idle time and generate predictions for efficient resource utilization.")

if st.button("Predict Idle Truck Time"):
    # Simulated predictive analytics output
    predicted_idle_time = round(np.random.uniform(2, 12), 2)
    idle_trucks = np.random.randint(5, 20)

    st.info(f"Predicted idle time for next delivery cycle: {predicted_idle_time} hours")
    st.metric(label="Idle Trucks Predicted", value=idle_trucks)

# Section 4: Data-Driven Insights & Recommendations
st.header("📈 Data-Driven Insights")
st.write("Key metrics to monitor logistics performance and efficiency.")

# Simulated Data
metrics = {
    "Idle Trucks (Today)": np.random.randint(5, 20),
    "Fuel Usage (liters)": round(np.random.uniform(800, 1500), 2),
    "Late Deliveries": np.random.randint(1, 5),
    "Vehicles Requiring Maintenance": np.random.randint(1, 10),
}

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Idle Trucks", value=metrics["Idle Trucks (Today)"])
col2.metric(label="Fuel Usage (liters)", value=f"{metrics['Fuel Usage (liters)']} L")
col3.metric(label="Late Deliveries", value=metrics["Late Deliveries"])
col4.metric(label="Maintenance Due", value=metrics["Vehicles Requiring Maintenance"])

st.subheader("🔍 AI-Driven Recommendations")
recommendations = [
    "Redistribute cargo to reduce truck idling.",
    "Schedule pending maintenance to avoid delivery delays.",
    "Optimize fuel routes to save costs based on current fuel prices.",
    "Analyze peak delivery times to manage traffic bottlenecks effectively.",
]
for rec in recommendations:
    st.write("- ", rec)

# Section 5: Interactive Visualization
st.subheader("📉 Fuel Usage and Idle Trucks Over Time")

# Generate Random Data for Visualization
days = np.arange(1, 31)  # Simulate 30 days of data
fuel_usage = np.random.uniform(800, 1500, size=len(days))
idle_trucks = np.random.randint(5, 20, size=len(days))

# Dataframe for Chart
df = pd.DataFrame({"Day": days, "Fuel Usage (liters)": fuel_usage, "Idle Trucks": idle_trucks})

# Create Line Chart
fig, ax1 = plt.subplots()

# Plot Fuel Usage
ax1.set_xlabel("Day")
ax1.set_ylabel("Fuel Usage (liters)", color="blue")
ax1.plot(df["Day"], df["Fuel Usage (liters)"], color="blue", marker="o", label="Fuel Usage")
ax1.tick_params(axis="y", labelcolor="blue")

# Plot Idle Trucks
ax2 = ax1.twinx()
ax2.set_ylabel("Idle Trucks", color="orange")
ax2.plot(df["Day"], df["Idle Trucks"], color="orange", marker="o", linestyle="--", label="Idle Trucks")
ax2.tick_params(axis="y", labelcolor="orange")

fig.tight_layout()
st.pyplot(fig)

# Section 6: Future Enhancements
st.header("🚀 Upcoming Features")
st.write(
    """
    - Advanced AI-driven driver performance analysis.
    - Real-time tracking of vehicle locations and fuel economy.
    - Integrated dashboards for live logistics monitoring.
    """
)
