import altair as alt
import streamlit as st
from services import auth, constants, fileio, plot

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

st.sidebar.header("Parameters")
number = st.sidebar.slider("Slider", 0, 100, 50)

st.write("## Section 1")
st.write(f"The slider value is `{number}`")
st.write(
    "See the streamlit [API reference](https://docs.streamlit.io/develop/api-reference)"
    " and [tutorials](https://docs.streamlit.io/get-started) for more information on"
    " how to use streamlit.",
)


st.write("## Section 2")
cols = st.columns(2)
feedback = fileio.load_csv(constants.DATA_PATH / "passenger_feedback.csv")
cols[0].write(feedback)
cols[1].altair_chart(
    alt.Chart(feedback)
    .mark_bar()
    .encode(alt.X("count()"), alt.Y("Passenger Feedback").title(None))
    .properties(title="Passenger feedback distribution"),
    use_container_width=True,
)
