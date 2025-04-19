import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
file_path = "resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
df = pd.read_csv(file_path)

# Data Cleaning
df['month'] = pd.to_datetime(df['month'])
df['year'] = df['month'].dt.year
df['quarter'] = df['month'].dt.to_period("Q")
df['price_per_sqm'] = df['resale_price'] / df['floor_area_sqm']

# Streamlit page configuration
st.set_page_config(page_title="Singapore Real Estate EDA", layout="wide")

# Title
st.title("Singapore Real Estate Market: Exploratory Data Analysis")

# Business Insights Header
st.subheader("Business Insights")

# 🔍 Insight 1: Median Resale Price Over Time (Interactive)
st.markdown("### 📈 Median Resale Price Over Years")
fig1 = px.line(
    df.groupby('year')['resale_price'].median().reset_index(),
    x='year', y='resale_price',
    title='Median Resale Price Over Years (Interactive)',
    labels={'resale_price': 'Median Resale Price (SGD)', 'year': 'Year'}
)
st.plotly_chart(fig1)

# 🔍 Insight 2: Price Distribution by Flat Type (Interactive)
st.markdown("### 🏠 Resale Price Distribution by Flat Type")
fig2 = px.box(
    df, x='flat_type', y='resale_price',
    title='Resale Price Distribution by Flat Type (Interactive)',
    labels={'resale_price': 'Resale Price (SGD)', 'flat_type': 'Flat Type'}
)
st.plotly_chart(fig2)

# 🔍 Insight 3: Average Price by Town (Interactive)
st.markdown("### 📍 Average Resale Price by Town")
avg_price_town_df = df.groupby('town', as_index=False)['resale_price'].mean().sort_values(by='resale_price', ascending=False)
fig3 = px.bar(
    avg_price_town_df, x='resale_price', y='town', orientation='h',
    title='Average Resale Price by Town (Interactive)',
    labels={'resale_price': 'Average Resale Price (SGD)', 'town': 'Town'}
)
st.plotly_chart(fig3)

# 🔍 Insight 4: Price per Square Meter by Flat Type (Interactive)
st.markdown("### 📏 Price per Square Meter by Flat Type")
fig4 = px.box(
    df, x='flat_type', y='price_per_sqm',
    title='Price per Square Meter by Flat Type (Interactive)',
    labels={'price_per_sqm': 'Price per sqm (SGD)', 'flat_type': 'Flat Type'}
)
st.plotly_chart(fig4)

# Conclusion
st.subheader("Conclusion")
st.markdown("""
- **Investors** may focus on undervalued towns with lower price per sqm.
- **Buyers** should consider timing, flat type, and location based on price trends and space needs.
- **Government planners** can track price pressure in mature estates and plan BTO/resale supply accordingly.
""")
