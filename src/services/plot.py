from __future__ import annotations

import re
from pathlib import Path

import streamlit as st


def extract_headings(
    file_path: str,
    pattern: str = r'st\.write\("## (.*?)"\)',
) -> list[str]:
    file = Path(file_path)
    with file.open(encoding="utf8") as f:
        file_content = f.read()
    return re.findall(pattern, file_content)


def table_of_contents(file_name: str) -> None:
    sections = extract_headings(file_name)
    toc_items = "".join(
        f'<li><a href="#{section.lower().replace(" ", "-")}">{section}</a></li>'
        for section in sections
    )
    st.sidebar.markdown(
        f"""
<style>
a,
a:visited {{
  color: rgba(49, 51, 63, 0.6)!important;
  text-decoration-line: none;
  font-weight: 500;
}}
</style>

## Table of Contents

<ul style="list-style-type: none">
{toc_items}
</ul>
""",
        unsafe_allow_html=True,
    )
