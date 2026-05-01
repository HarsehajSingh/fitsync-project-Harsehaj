import streamlit as st
from modules.processor import process_data
import plotly.express as px

# Page config
st.set_page_config(layout="wide", page_title="FitSync Dashboard")

# Caching function
@st.cache_data(ttl=600)
def cached_process_data():
    return process_data()

# Title
st.title("FitSync - Personal Health Analytics Dashboard")

# Sidebar
st.sidebar.header("Filters")

time_range = st.sidebar.selectbox(
    "Select Time Range",
    ["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

def main():
    # Load data
    df = cached_process_data()

    # Sort by Date (important for charts)
    df = df.sort_values("Date")

    # Filter data
    if time_range == "Last 7 Days":
        filtered_df = df.tail(7)
    elif time_range == "Last 30 Days":
        filtered_df = df.tail(30)
    else:
        filtered_df = df

    # 📊 Metrics
    avg_steps = filtered_df['Steps'].mean()
    avg_sleep = filtered_df['Sleep_Hours'].mean()
    avg_recovery = filtered_df['Recovery_Score'].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Steps", f"{avg_steps:.0f}")

    with col2:
        st.metric("Average Sleep Hours", f"{avg_sleep:.1f}")

    with col3:
        st.metric("Average Recovery Score", f"{avg_recovery:.1f}")

    # 📈 Charts
    st.subheader("Health Trends")

    col_left, col_right = st.columns(2)

    # Recovery + Sleep Trend
    with col_left:
        fig1 = px.line(
            filtered_df,
            x="Date",
            y=["Recovery_Score", "Sleep_Hours"],
            title="Recovery Score & Sleep Trend"
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Recovery vs Steps
    with col_right:
        fig2 = px.scatter(
            filtered_df,
            x="Steps",
            y="Recovery_Score",
            color="Sleep_Hours",
            title="Recovery Score vs Steps"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # More charts
    col_left2, col_right2 = st.columns(2)

    # Recovery vs Heart Rate
    with col_left2:
        fig3 = px.scatter(
            filtered_df,
            x="Heart_Rate_bpm",
            y="Recovery_Score",
            title="Recovery vs Heart Rate"
        )
        st.plotly_chart(fig3, use_container_width=True)

    # Calories trend
    with col_right2:
        fig4 = px.line(
            filtered_df,
            x="Date",
            y="Calories_Burned",
            title="Calories Burned Trend"
        )
        st.plotly_chart(fig4, use_container_width=True)

    # 🧠 Insight Section
    st.subheader("AI Insight")

    if avg_sleep < 6:
        st.warning("⚠️ Low sleep detected. Improve sleep for better recovery.")
    elif avg_steps < 6000:
        st.info("🚶 Increase your daily steps for better fitness.")
    else:
        st.success("✅ Great job! Your health metrics are balanced.")

# Run app
if __name__ == "__main__":
    main()