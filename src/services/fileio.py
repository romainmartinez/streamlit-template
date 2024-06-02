from pathlib import Path

import pandas as pd
import streamlit as st
from bin import generate_data


@st.cache_data
def load_csv(
    data_path: Path,
) -> pd.DataFrame:
    if not data_path.exists():
        generate_data.main()
    return pd.read_csv(data_path.expanduser(), low_memory=False)
