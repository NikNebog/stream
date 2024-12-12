import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
from PIL import Image
import os

image = Image.open('img/images.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "images (1).svg")
pages = ['Home', 'Project1', 'Project2', 'Project3']

styles = {
    "nav": {
        "background-color": "royalblue",
        "display": "flex",
        "justify-content": "center",
        "position": "relative"
    },
    "img": {
        "position": "absolute",
        "left": "10px",
        "top": "4px",
        "width": "150px",
        "height": "40px",
    },
    "span": {
        "color": "white",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    styles=styles,
    logo_path=logo_path,
    options=options
)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
