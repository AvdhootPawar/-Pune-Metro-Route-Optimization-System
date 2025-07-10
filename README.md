# 🚇 Pune-Metro-Route-Optimization-System

---

The Pune-Metro-Route-Optimization-System is an intelligent web-based application designed to streamline urban travel by providing efficient route planning within a simulated metro/bus network. It helps users discover the shortest paths, estimate travel times, and calculate fares, making daily commutes more predictable and convenient.

---

## ✨ Core Functionalities

This system offers intuitive tools to optimize your journey:

### 1. Route Planning

* **Source & Destination Selection:** Users can easily select their desired starting point and final destination from available transit hubs.
* **Optimal Path Calculation:** Utilizes **Dijkstra's algorithm** to find the most efficient route (based on distance) between the selected points.

### 2. Travel Estimation

* **Distance Calculation:** Provides the total distance of the optimized route in kilometers.
* **Time Estimation:** Estimates the approximate travel time in minutes for the suggested route.
* **Fare Calculation:** Computes the estimated fare based on the calculated distance.

---

## 🔑 Key Features

* **Efficient Pathfinding:** Implements a robust Dijkstra's algorithm to ensure the discovery of the shortest and most efficient routes.
* **Intuitive User Interface:** Built with **Streamlit** for a clean, user-friendly, and interactive web application experience.
* **Comprehensive Trip Details:** Offers a complete overview of the journey, including path, distance, time, and fare, at a glance.
* **Input Validation:** Prevents common errors by prompting users if the source and destination selected are identical.
* **Modular Design:** The project's structure (separate modules for graph data, pathfinding logic, and utilities) promotes maintainability and scalability.

---

## 🛠️ Technical Stack

### Backend Logic

* **Python:** The core programming language.
* **Dijkstra's Algorithm Implementation (`pathfinder.py`):** Efficiently calculates the shortest path through the transit graph.
* **Graph Data Representation (`graph_data.py`):** Defines the transit network, including distances and times between nodes.
* **Fare Calculation Utility (`utils.py`):** Contains the logic for dynamically calculating fares based on route distance.

### Frontend

* **Streamlit:** Used to create the interactive web application, providing a straightforward interface for users to select locations and view route details.

---

## 🌱 Vision & Impact

The Pune-Metro-Route-Optimization-System aims to enhance urban mobility by providing a reliable and easy-to-use tool for commuters. By optimizing travel routes and offering clear estimations, it can contribute to:

* **Reduced Commute Times:** Helping users find the most efficient way to travel.
* **Improved Planning:** Empowering commuters with accurate information on distance, time, and cost.
* **Efficient Resource Utilization:** Potentially aiding urban planners in understanding and improving transit flow.

This project showcases a practical application of graph algorithms and data structures to solve real-world logistical challenges in public transportation.

---

## 📸 Screenshots

Here are a few glimpses of the Pune-Metro-Route-Optimization-System in action. To add your own screenshots, replace the `alt text` and `path/to/your/image.png` with your actual details.

### Main Interface

![Screenshot of the Main User Interface](assets/screenshots/main_interface.png)
*Example: A clear shot of the source and destination selection dropdowns.*

### Route Found Display

![Screenshot of Route Found Display](assets/screenshots/route_found.png)
*Example: Showing the output with the optimized route, distance, time, and fare.*

### Error Message Example

![Screenshot of Error Message](assets/screenshots/error_message.png)
*Example: Demonstrating the warning for selecting the same source and destination.*
