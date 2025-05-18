import streamlit as st
from streamlit_folium import st_folium
from typing import Optional, Tuple

from lib.map_utils import render_route_map

def draw_sidebar() -> None:
    """
    Render the application sidebar with project information.
    
    Includes:
    - Project title and algorithm information
    - Course and instructor details
    - Contributor list
    """
    st.sidebar.title("Geospatial Emergency Hospital Routing")
    st.sidebar.markdown("Using Dijkstra's Algorithm")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("**Course:** Design & Analysis of Algorithms")
    st.sidebar.markdown("**Instructor:** Dr. Mohamed Ghetas")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("**Contributors:**")
    contributors = [
        "Mohammed Haitham", "Ahmed Yasser Eissa", "Farah Mohamed",
        "Karim Atwa", "Mahros El-Qabasy", "Ahmed Yasser Lotfy",
        "Hassan Mohamed", "Abdallah Tarek"
    ]
    for contributor in contributors:
        st.sidebar.markdown(f"- {contributor}")
    st.sidebar.markdown("---")

def draw_main() -> None:
    """
    Render the main application title and instructions.
    """
    st.title("Nearest Hospital Route Finder")
    st.write("Click on the map to select your location.")

def draw_location_info(user_loc: Tuple[float, float]) -> None:
    """
    Display the selected user location coordinates.
    
    Args:
        user_loc: Tuple of (latitude, longitude) coordinates
    """
    st.subheader("Selected Location")
    st.markdown(f"Latitude: **{user_loc[0]:.4f}**, Longitude: **{user_loc[1]:.4f}**")

def draw_hospital_info(hospital_name: str, straight_dist: float) -> None:
    """
    Display information about the nearest hospital.
    
    Args:
        hospital_name: Name of the nearest hospital
        straight_dist: Straight-line distance to hospital in kilometers
    """
    st.subheader("Nearest Hospital")
    st.markdown(f"**{hospital_name}**")
    st.info(f"Straight-line distance: **{straight_dist:.2f} km**")

def draw_route_info(
    user_loc: Tuple[float, float],
    hospital_loc: Tuple[float, float],
    hospital_name: str,
    geometry: Optional[dict],
    road_dist: float,
    duration: float
) -> None:
    """
    Display the driving route information and visualization.
    
    Args:
        user_loc: User's (latitude, longitude) coordinates
        hospital_loc: Hospital's (latitude, longitude) coordinates
        hospital_name: Name of the destination hospital
        geometry: Route geometry from OpenRouteService (GeoJSON format)
        road_dist: Driving distance in kilometers
        duration: Estimated travel time in minutes
    """
    if geometry:
        # Render the interactive route map
        route_map = render_route_map(user_loc, hospital_loc, hospital_name, geometry)
        st.subheader("Driving Route")
        st_folium(route_map, height=600, width="100%", key="route_map")
        
        # Display route metrics
        st.info(f"Driving distance: **{road_dist:.2f} km**")
        st.info(f"Estimated time: **{duration:.1f} min**")
    else:
        st.warning("Could not retrieve driving route information.")

def draw_no_selection() -> None:
    """
    Display instructions when no location has been selected.
    """
    st.info("Click on the map to select your starting location.")