import numpy as np
import pandas as pd
from typing import Tuple

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on Earth using the Haversine formula.
    
    Args:
        lat1: Latitude of first point in degrees
        lon1: Longitude of first point in degrees
        lat2: Latitude of second point in degrees
        lon2: Longitude of second point in degrees
    
    Returns:
        Distance between the points in kilometers
    
    Reference:
        https://en.wikipedia.org/wiki/Haversine_formula
    """
    EARTH_RADIUS = 6371.0  # Earth's average radius in kilometers
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Calculate differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    return EARTH_RADIUS * c

def find_nearest_hospital(user_loc: Tuple[float, float], df: pd.DataFrame) -> Tuple[str, float, Tuple[float, float]]:
    """
    Identify the nearest hospital to the user's location.
    
    Args:
        user_loc: Tuple of user's (latitude, longitude) coordinates
        df: DataFrame containing hospital location data
    
    Returns:
        Tuple containing:
        - Hospital name
        - Distance in kilometers
        - Hospital coordinates (latitude, longitude)
    
    Raises:
        ValueError: If input DataFrame is invalid or missing required columns
    """
    # Validate input DataFrame
    required_columns = {"Latitude", "Longitude", "Hospital Name"}
    if df.empty or not required_columns.issubset(df.columns):
        raise ValueError("Invalid hospital DataFrame: Missing required columns or empty.")
    
    # Calculate distances to all hospitals
    distances = df.apply(
        lambda row: haversine(user_loc[0], user_loc[1], row["Latitude"], row["Longitude"]), 
        axis=1
    )
    
    # Find nearest hospital
    nearest_idx = distances.idxmin()
    nearest_row = df.loc[nearest_idx]
    
    return (nearest_row["Hospital Name"], distances[nearest_idx], 
            (nearest_row["Latitude"], nearest_row["Longitude"]))