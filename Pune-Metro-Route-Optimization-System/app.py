import streamlit as st
from metro_data import load_graph, dijkstra, calculate_fare

st.set_page_config(page_title="Pune Metro Planner", page_icon="🚇")
st.title("🚇 Smart Pune Metro Route Planner")

graph = load_graph("stations.csv")
stations = sorted(graph.keys())

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("Select Source Station", stations)
with col2:
    destination = st.selectbox("Select Destination Station", stations)

if st.button("Find Route"):
    if source == destination:
        st.warning("Source and destination must be different.")
    else:
        path, total_time = dijkstra(graph, source, destination)
        if path:
            st.success("Route Found!")
            st.markdown("** → ** ".join(path))
            fare = calculate_fare(total_time)
            st.info(f"🕒 Estimated Time: {round(total_time, 1)} minutes")
            st.info(f"💰 Fare: ₹{fare}")
        else:
            st.error("No route found.")
