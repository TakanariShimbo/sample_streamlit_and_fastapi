import streamlit as st


class TitleHandler:
    @staticmethod
    def set_title(icon: str, title: str):
        st.set_page_config(
            page_title=title,
            page_icon=icon,
        )
        st.write(f"## {icon} {title}")
        st.sidebar.header(title)
