from __future__ import annotations

import streamlit as st

from .constants import APP_PASSWORD, IS_LOCAL


def is_authenticated() -> bool | None:
    if IS_LOCAL or st.session_state.get("authenticated", False):
        return True
    login()
    st.error("Not authenticated")
    st.stop()
    return None


@st.experimental_dialog("Login")
def login() -> None:
    with st.form(key="login_form"):
        password = st.text_input(
            "Password",
            type="password",
        )
        if st.form_submit_button("Submit", type="primary", use_container_width=True):
            if password == APP_PASSWORD:
                st.session_state.authenticated = True
                st.toast("✅ Logged in")
                st.rerun()
            else:
                st.error("Wrong password")
