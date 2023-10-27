import streamlit as st
import plotly.express as px

from handlers.login_handler import LoginHandler
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


# Set Titles
TitleTemplate.set_page_configs(icon="📊", title="DataFrame")


# check login
login_handler = LoginHandler()
NotLoginTemplate.display_not_login_contents(
    check_is_login_callback=login_handler.check_is_login,
)


# Contents
@st.cache_data
def get_original_countries_data():
    return px.data.gapminder()

try:
    original_countries_df = get_original_countries_data()

    st.write("### GDP per Capita Over Time")
    selected_countries = st.multiselect(
        label="Choose countries", 
        options=original_countries_df["country"].unique(), # whole countries list
        default=["China", "United States"]
    )

    if not selected_countries:
        st.error("Please select at least one country.")
    else:
        parse_indexes = original_countries_df["country"].isin(selected_countries)
        parse_columns = ["country", "year", "gdpPercap"]
        filtered_countries_df = original_countries_df.loc[parse_indexes, parse_columns]
        st.write("#### Table of selected countories")
        st.write(filtered_countries_df)
        
        fig = px.line(filtered_countries_df, x="year", y="gdpPercap", color="country", labels={"year": "Year", "gdpPercap": "GDP per Capita"})
        st.write("#### Chat of selected countories")
        st.plotly_chart(fig, use_container_width=True)

except:
    st.error("Countries data was couldn't loaded.")
