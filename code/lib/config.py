import streamlit as st
from typing import Literal

def configure_page():
    """Configure all Streamlit page settings with beautiful defaults"""
    st.set_page_config(
        layout="wide",
        page_title="Emergency Hospital Routing",
        page_icon="🦺",
        initial_sidebar_state="collapsed",
        menu_items=None
    )

def apply_dark_theme():
    """Apply custom dark theme with beautiful styling"""
    st.markdown("""
    <style>
        /* Main dark theme */
        [data-testid="stAppViewContainer"] {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        
        /* Beautiful headers */
        h1 {
            color: #FF4B4B;
            border-bottom: 1px solid #444;
            padding-bottom: 10px;
        }
        
        h2 {
            color: #4B9DFF;
        }
        
        /* Cards and containers */
        [data-testid="stExpander"] {
            background-color: #1A1A1A;
            border: 1px solid #444;
            border-radius: 8px;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 4px;
            border: none;
            padding: 8px 16px;
            font-weight: 500;
        }
        
        .stButton>button:hover {
            background-color: #E63B3B;
        }
        
        /* Input widgets */
        .stTextInput>div>div>input,
        .stNumberInput>div>div>input,
        .stSelectbox>div>div>select {
            background-color: #1A1A1A;
            color: white;
            border: 1px solid #444;
        }
        
        /* Remove padding around main content */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* Hide all unnecessary elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Beautiful map container */
        .folium-map {
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
    """, unsafe_allow_html=True)

def configure_sidebar_style():
    """Style the sidebar with dark theme"""
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1A1A1A !important;
            border-right: 1px solid #444;
        }
        
        .sidebar .sidebar-content {
            background-color: #1A1A1A;
        }
        
        [data-testid="stSidebarUserContent"] {
            padding: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

def apply_custom_font(font: Literal["sans", "serif", "monospace"] = "sans"):
    """Apply a custom font to the entire app"""
    font_family = {
        "sans": "Helvetica, Arial, sans-serif",
        "serif": "Georgia, serif",
        "monospace": "Courier New, monospace"
    }.get(font, "Helvetica, Arial, sans-serif")
    
    st.markdown(f"""
    <style>
        html, body, [class*="css"] {{
            font-family: {font_family};
        }}
    </style>
    """, unsafe_allow_html=True)

def configure_dataframe_style():
    """Style pandas DataFrames with dark theme"""
    st.markdown("""
    <style>
        .stDataFrame {
            background-color: #1A1A1A;
        }
        
        table.dataframe {
            background-color: #1A1A1A;
            color: #FAFAFA;
            border: 1px solid #444;
        }
        
        table.dataframe th {
            background-color: #2A2A2A;
            color: #FAFAFA;
        }
        
        table.dataframe tr:nth-child(even) {
            background-color: #252525;
        }
        
        table.dataframe tr:hover {
            background-color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

def initialize_ui():
    """Initialize all UI configurations at once"""
    configure_page()
    apply_dark_theme()
    configure_sidebar_style()
    apply_custom_font("sans")
    configure_dataframe_style()