import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(layout="wide")

st.title("🧠 Disability among Scheduled Caste (SC) Population – India Census 2011")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\MY PC\Downloads\Data analyst\Python\india_census_project\saved data\disability_data.csv")
    with open("india_states.json", "r") as f:
        geojson = json.load(f)
    return df, geojson

df, india_geojson = load_data()

# Choropleth
st.subheader("🗺️ Choropleth Heatmap – Total Disabled (SC) by State")

fig = px.choropleth(
    df,
    geojson=india_geojson,
    featureidkey="properties.ST_NM",
    locations="State",
    color="Total_Disabled",
    color_continuous_scale="Reds",
    title="Total Disabled Persons (SC) by State",
)
fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

# Data preview
with st.expander("📊 View Raw Disability Data"):
    st.dataframe(df)
