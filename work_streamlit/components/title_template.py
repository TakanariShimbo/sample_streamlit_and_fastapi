import streamlit as st


class TitleTemplate:
    @staticmethod
    def set_page_configs(icon: str, title: str):
        st.set_page_config(
            page_title=title,
            page_icon=icon,
        )
        st.write(f"## {icon}{title}")
        st.sidebar.header(title)
