import re

import streamlit as st


def extract_headings(file_path, pattern: str = r'st\.write\("## (.*?)"\)'):
    with open(file_path, encoding="utf8") as file:
        file_content = file.read()
    return re.findall(pattern, file_content)


def table_of_contents(file_name: str) -> None:
    sections = extract_headings(file_name)
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
{''.join(f'<li><a href="#{section.lower().replace(" ", "-")}">{section}</a></li>' for section in sections)}
</ul>
""",
        unsafe_allow_html=True,
    )
