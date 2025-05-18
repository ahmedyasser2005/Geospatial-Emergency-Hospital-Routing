import pandas as pd
import streamlit as st

from lib.config import initialize_ui
from lib.data_loader import load_hospitals
from lib.gui_drawer import (draw_main, draw_no_selection, draw_sidebar, draw_location_info, draw_hospital_info, draw_route_info)
from lib.interaction_handler import process_user_interaction
from lib.map_utils import render_initial_map

def main():
    """
    Main application entry point that orchestrates the Streamlit interface.
    
    Workflow:
    1. Initialize sidebar UI
    2. Load hospital data
    3. Render main interface
    4. Process user interactions
    5. Display appropriate results
    """
    # Initialize sidebar with project information
    draw_sidebar()
    
    # Load hospital location data with error handling
    try:
        hospital_locations = load_hospitals()
    except (FileNotFoundError, pd.errors.EmptyDataError, Exception) as e:
        st.error(f"Failed to load hospital data: {str(e)}")
        return
        
    # Render main application interface
    draw_main()
    
    # Display interactive map and get user interactions
    folium_result = render_initial_map()    
    interaction_data = process_user_interaction(folium_result, hospital_locations)
    
    # Process and display results based on user interaction
    if interaction_data:
        try:
            user_loc, name, straight_dist, hospital_loc, geometry, road_dist, duration = interaction_data
            draw_location_info(user_loc)
            draw_hospital_info(name, straight_dist)
            draw_route_info(user_loc, hospital_loc, name, geometry, road_dist, duration)
        except ValueError as e:
            st.error(str(e))
    else:
        draw_no_selection()

if __name__ == "__main__":
    initialize_ui()
    main()