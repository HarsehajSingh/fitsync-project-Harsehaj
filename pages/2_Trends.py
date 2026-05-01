import streamlit as st
from modules.processor import process_data
import plotly.express as px
import pandas as pd

# Caching function
@st.cache_data(ttl=600)
def cached_process_data():
    return process_data()

# Title
st.title("Trends & Insights")

# Sidebar
st.sidebar.header("Filters")

time_range = st.sidebar.selectbox(
    "Select Time Range",
    ["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Load data
df = cached_process_data()

# Sort by date
df = df.sort_values("Date")

# Filter
if time_range == "Last 7 Days":
    filtered_df = df.tail(7)
elif time_range == "Last 30 Days":
    filtered_df = df.tail(30)
else:
    filtered_df = df

# 📊 Summary Statistics
st.subheader("Summary Statistics")

columns = ['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']

for col in columns:
    st.write(f"**{col.replace('_', ' ')}**")
    st.write({
        "Mean": round(filtered_df[col].mean(), 2),
        "Min": round(filtered_df[col].min(), 2),
        "Max": round(filtered_df[col].max(), 2)
    })

# 📈 Monthly Recovery Trend
filtered_df['Month'] = filtered_df['Date'].dt.to_period('M').astype(str)

monthly_avg = filtered_df.groupby('Month')['Recovery_Score'].mean().reset_index()

fig = px.line(
    monthly_avg,
    x='Month',
    y='Recovery_Score',
    title="Monthly Average Recovery Score"
)

st.plotly_chart(fig, use_container_width=True)

# 📊 Histograms
st.subheader("Distribution of Metrics")

for col in columns:
    fig = px.histogram(
        filtered_df,
        x=col,
        nbins=20,
        title=f"Distribution of {col.replace('_', ' ')}"
    )
    st.plotly_chart(fig, use_container_width=True)