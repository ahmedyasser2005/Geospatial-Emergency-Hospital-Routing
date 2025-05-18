import os
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import streamlit as st

def check_local_file(hospital_file: str) -> pd.DataFrame | None:
    """
    Check for and load local hospital data file if it exists.
    
    Args:
        hospital_file: Path to the local hospital data CSV file
    
    Returns:
        Loaded DataFrame if file exists, None otherwise
    """
    if os.path.exists(hospital_file):
        return pd.read_csv(hospital_file)
    return None

def download_from_kaggle(hospital_file: str) -> pd.DataFrame:
    """
    Download hospital dataset from Kaggle and save locally.
    
    Args:
        hospital_file: Destination path for the downloaded data
    
    Returns:
        DataFrame containing the downloaded hospital data
    
    Raises:
        FileNotFoundError: If Kaggle download fails
    """
    try:
        # Download dataset from Kaggle using the KaggleHub API
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "andrewmvd/us-hospital-locations",
            "data"
        )
        
        # Ensure directory exists and save data
        os.makedirs(os.path.dirname(hospital_file), exist_ok=True)
        df.to_csv(hospital_file, index=False)
        return df
    
    except Exception as e:
        raise FileNotFoundError(
            f"Failed to download dataset from Kaggle: {str(e)}\n"
            "Please ensure your Kaggle API token is configured in ~/.kaggle/kaggle.json"
        )

def clean_hospital_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize hospital location data.
    
    Args:
        df: Raw hospital data DataFrame
    
    Returns:
        Cleaned DataFrame with standardized columns
    
    Raises:
        pd.errors.EmptyDataError: If data is empty after cleaning
    """
    # Select and rename relevant columns
    df = df[["NAME", "LATITUDE", "LONGITUDE"]].dropna()
    df.columns = ["Hospital Name", "Latitude", "Longitude"]
    
    # Validate we have data remaining
    if df.empty:
        raise pd.errors.EmptyDataError("Hospital data is empty after cleaning.")
    
    return df

@st.cache_data
def load_hospitals(hospital_file: str = "data/us_hospital_locations.csv") -> pd.DataFrame:
    """
    Load hospital location data from local cache or Kaggle if not available.
    
    Args:
        hospital_file: Path to local hospital data file (default: "data/us_hospital_locations.csv")
    
    Returns:
        Cleaned DataFrame with hospital names and coordinates
    
    Raises:
        FileNotFoundError: If data cannot be loaded from any source
        pd.errors.EmptyDataError: If loaded data is empty
        Exception: For unexpected errors during loading
    """
    try:
        # Attempt to load local data file
        df = check_local_file(hospital_file)

        # Fall back to Kaggle download if local file not found
        if df is None:
            df = download_from_kaggle(hospital_file)

        # Clean and standardize the data
        return clean_hospital_data(df)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error accessing hospital data file: {str(e)}")
    
    except pd.errors.EmptyDataError as e:
        raise pd.errors.EmptyDataError("Hospital data file is empty or contains no valid data.")
    
    except Exception as e:
        raise Exception(f"Unexpected error while loading hospital data: {str(e)}")