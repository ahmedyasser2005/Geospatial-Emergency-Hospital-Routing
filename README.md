# Geospatial Emergency Hospital Routing

## Overview

This project is a geospatial routing application designed to provide efficient emergency response in healthcare. It uses Dijkstra's algorithm to determine the nearest hospital to a user-defined location and calculates the optimal driving route.

## Visuals

#### Application Interface
 ![A screenshot of the main application interface](docs\imgs\1.png?raw=true)

#### Route Display
 ![A screenshot of the application displaying a calculated route](docs\imgs\2.png?raw=true)

## Features

* **Nearest Hospital Calculation:** The application implements Dijkstra's algorithm to find the shortest path to the nearest hospital.
* **Geospatial Data Integration:** The application integrates hospital locations and road network information.
* **User-Friendly Interface:** The application allows users to select their location on a map and view the optimal route to the nearest hospital.
* **Route Information Display:** The application displays key route information, including distance and estimated travel time.

## Technologies Used

* Python
* Streamlit
* Pandas
* Folium
* OpenRouteService API

## Usage

1.  Open the application in your web browser.
2.  Click on the map to select your current location.
3.  The application will display the nearest hospital, the optimal driving route, the distance, and the estimated travel time.

## Project Structure

* `📁code`: Main application entry point.
    * `📁lib`: Main application entry point.
        * `🐍config.py`: Streamlit page configuration and custom styling.
        * `🐍data_loader.py`: Hospital location data loading and cleaning.
        * `🐍gui_drawer.py`: User interface elements rendering.
        * `🐍interaction_handler.py`: User interaction processing and route calculation coordination.
        * `🐍map_utils.py`: Folium map initialization and rendering.
        * `🐍route_service.py`: Optimal driving route calculation using OpenRouteService API.
        * `🐍utils.py`: Utility functions, including Haversine distance calculation and nearest hospital finding.
    * `🐍app.py`: Main application entry point.
* `📅data/us_hospital_locations.csv`: Local copy of the hospital location data.
* `🛠️requirements.txt`: Project dependencies.

## Team
- Mohammed Haitham
- Ahmed Yasser Eissa
- Farah Mohamed
- Karim Atwa
- Mahros El-Qabasy
- Ahmed Yasser Lotfy
- Hassan Mohamed
- Abdallah Tarek