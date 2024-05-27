import streamlit as st
from services import auth, plot

# Page config
auth.is_authenticated()

st.set_page_config(
    page_title="First page",
    page_icon="static/cae_logo.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo("static/cae_logo.svg")


st.write(
    """# First page
Page description.
""",
)

plot.table_of_contents(__file__)

# Page parameters
st.sidebar.header("Parameters")
st.sidebar.slider("Slider")

# first section
st.write("## First header")

# second section
st.write("## Second header")
