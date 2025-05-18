import pandas as pd
from typing import Optional, Tuple

from lib.route_service import get_best_route
from lib.utils import find_nearest_hospital

def process_user_interaction(
    folium_result: Optional[dict], 
    hospital_locations: pd.DataFrame
) -> Optional[Tuple[Tuple[float, float], str, float, Tuple[float, float], Optional[dict], float, float]]:
    """
    Process user map interactions and coordinate route calculation.
    
    Args:
        folium_result: Folium interaction data containing click information
        hospital_locations: DataFrame of hospital location data
    
    Returns:
        Tuple containing route information if valid interaction occurred:
        - User coordinates (lat, long)
        - Hospital name
        - Straight-line distance (km)
        - Hospital coordinates (lat, long)
        - Route geometry (GeoJSON)
        - Road distance (km)
        - Estimated duration (min)
        Returns None if no valid interaction
    
    Raises:
        ValueError: If hospital lookup fails
    """
    # Check for valid map interaction
    if not folium_result or not folium_result.get("last_clicked"):
        return None

    # Extract user coordinates from click event
    user_loc = (
        folium_result["last_clicked"]["lat"],
        folium_result["last_clicked"]["lng"]
    )
    
    try:
        # Find nearest hospital and calculate route
        name, straight_dist, hospital_loc = find_nearest_hospital(user_loc, hospital_locations)
        geometry, road_dist, duration = get_best_route(user_loc, hospital_loc)
        
        return user_loc, name, straight_dist, hospital_loc, geometry, road_dist, duration
    
    except ValueError as e:
        raise ValueError(f"Error finding nearest hospital: {str(e)}")