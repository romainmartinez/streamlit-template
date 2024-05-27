import streamlit as st

title = "📖 CAE Streamlit template"

st.set_page_config(
    page_title=title,
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write(f"# {title}")
