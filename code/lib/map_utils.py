import folium
import streamlit as st
from streamlit_folium import st_folium
from typing import Optional

def initialize_map() -> folium.Map:
    """
    Create and configure the initial Folium map centered on the continental US.
    
    Returns:
        Configured Folium map object with default view
    """
    # Center on continental US with appropriate zoom level
    return folium.Map(location=[39.8283, -98.5795], zoom_start=5)

def get_initial_map() -> folium.Map:
    """
    Retrieve or initialize the base map from Streamlit session state.
    
    Returns:
        The initialized Folium map object
    
    Note:
        Uses Streamlit session state to maintain map instance across reruns
    """
    if "m_initial" not in st.session_state:
        st.session_state.m_initial = initialize_map()
    
    return st.session_state.m_initial

def render_initial_map() -> Optional[dict]:
    """
    Display the interactive Folium map and capture user interactions.
    
    Returns:
        Dictionary containing map interaction data or None if no interactions
    
    Note:
        The returned data includes last clicked position and other interaction details
    """
    return st_folium(
        get_initial_map(),
        height=600,
        width="100%",
        key="initial_map"
    )

def render_route_map(
    user_loc: tuple, 
    hospital_loc: tuple, 
    hospital_name: str, 
    geometry: dict
) -> folium.Map:
    """
    Generate a Folium map displaying the route between user and hospital locations.
    
    Args:
        user_loc: Tuple of user's (latitude, longitude) coordinates
        hospital_loc: Tuple of hospital's (latitude, longitude) coordinates
        hospital_name: Name of the destination hospital
        geometry: Route geometry from OpenRouteService (GeoJSON format)
    
    Returns:
        Configured Folium map object with route and markers
    
    Note:
        - Uses Font Awesome icons for location markers
        - Automatically fits viewport to show entire route
    """
    # Initialize map centered on user location
    route_map = folium.Map(location=user_loc, zoom_start=12)
    
    # Configure markers with Font Awesome icons
    user_icon = folium.Icon(color="blue", icon="user", prefix="fa")
    hospital_icon = folium.Icon(color="red", icon="hospital", prefix="fa")
    
    # Add location markers
    folium.Marker(user_loc, tooltip="Your Location", icon=user_icon).add_to(route_map)
    folium.Marker(
        hospital_loc, 
        tooltip=hospital_name, 
        icon=hospital_icon
    ).add_to(route_map)
    
    # Add route geometry
    folium.GeoJson(
        geometry,
        name="Route",
        style_function=lambda feature: {
            "color": "green",
            "weight": 5,
            "opacity": 0.7
        }
    ).add_to(route_map)
    
    # Add layer control and fit bounds
    folium.LayerControl().add_to(route_map)
    route_map.fit_bounds([user_loc, hospital_loc], padding=(50, 50))
    
    return route_map