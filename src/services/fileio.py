from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_csv(
    data_path: Path,
) -> pd.DataFrame:
    return pd.read_csv(data_path.expanduser(), low_memory=False)
