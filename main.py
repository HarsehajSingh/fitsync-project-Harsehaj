import streamlit as st
from modules.processor import process_data
import plotly.express as px

st.title("FitSync - Personal Health Analytics Dashboard")

st.markdown("""
### 💡 About FitSync

**FitSync** is a personal health analytics dashboard designed to help users monitor and improve their overall well-being using data-driven insights.  
It integrates key health metrics such as **daily steps, sleep duration, heart rate, and calorie expenditure** to evaluate physical recovery and activity patterns.

The system computes a **Recovery Score (0–100)** that reflects how well the body is recovering.

### 🔍 Key Features:
- 📊 Health data visualization  
- 🧠 Recovery Score calculation  
- 📅 Time-based filtering  
- 📈 Trend analysis  

### 🎯 Purpose:
To convert raw health data into **meaningful insights** for better lifestyle decisions.
---
""")

theme = st.sidebar.radio("Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)