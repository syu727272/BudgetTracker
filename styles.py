import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the Streamlit app"""
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .stForm {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        
        .stButton button {
            width: 100%;
            background-color: #FF4B4B;
            color: white;
        }
        
        .stButton button:hover {
            background-color: #ff3333;
        }
        
        .css-1d391kg {
            padding: 20px;
        }
        
        .streamlit-expanderHeader {
            background-color: #f8f9fa;
        }
        
        div[data-testid="stHorizontalBlock"] > div:first-child {
            border-right: 1px solid #e6e6e6;
        }
        </style>
    """, unsafe_allow_html=True)
