import os
from typing import Optional, Tuple

import openrouteservice as ors
import streamlit as st
from dotenv import load_dotenv

# Load environment variables and initialize OpenRouteService client
load_dotenv()
client = ors.Client(key=os.getenv("API_KEY"))

def get_best_route(user_location: Tuple[float, float], hospital_location: Tuple[float, float]) -> Tuple[Optional[dict], float, float]:
    """
    Calculate the optimal driving route between user and hospital locations using OpenRouteService API.
    
    Args:
        user_location: Tuple containing user's (latitude, longitude) coordinates
        hospital_location: Tuple containing hospital's (latitude, longitude) coordinates
    
    Returns:
        Tuple containing:
        - Route geometry (GeoJSON format) or None if route not found
        - Driving distance in kilometers
        - Estimated duration in minutes
    
    Raises:
        ors.exceptions.ApiError: If OpenRouteService API request fails
        Exception: For unexpected errors during route calculation
    """
    try:
        # Convert coordinates to OpenRouteService format (longitude, latitude)
        coords = [user_location[::-1], hospital_location[::-1]]
        
        # Request driving directions from OpenRouteService
        route = client.directions(
            coords,
            profile="driving-car",
            format="geojson"
        )

        # Validate route response
        if not route or "features" not in route or not route["features"]:
            st.error("No route found. Please verify locations or API key.")
            return None, 0.0, 0.0

        # Extract route geometry and properties
        geometry = route["features"][0]["geometry"]
        properties = route["features"][0].get("properties", {}).get("segments", [{}])[0]
        
        # Convert distance to km and duration to minutes
        distance_km = properties.get("distance", 0) / 1000.0
        duration_min = properties.get("duration", 0) / 60.0
        
        # Warn if detailed properties are missing
        if not properties:
            st.warning("Route found but no detailed segment properties available.")
        
        return geometry, distance_km, duration_min

    except ors.exceptions.ApiError as e:
        st.error(f"OpenRouteService API Error: {str(e)}")
        st.error("Please verify your API key and network connection.")
        return None, 0.0, 0.0
    
    except Exception as e:
        st.error(f"Unexpected error while calculating route: {str(e)}")
        return None, 0.0, 0.0