import streamlit as st

def apply_style():
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/1809644/pexels-photo-1809644.jpeg");
    background-size: cover;
    }
    [data-testid="stHeader"] {
    background-image: url("https://images.pexels.com/photos/1809644/pexels-photo-1809644.jpeg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
