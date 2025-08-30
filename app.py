import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config (must be the first Streamlit command)
st.set_page_config(page_title="Marketing Performance Dashboard", layout="wide")

# Load or create sample data
@st.cache_data
def load_data():
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Sales": [12000, 15000, 18000, 17000, 21000, 25000, 30000, 28000, 26000, 27000, 31000, 35000],
        "Marketing Spend": [4000, 5000, 6000, 5500, 7000, 8000, 9000, 8500, 7500, 7800, 8200, 9500],
        "Leads Generated": [120, 150, 180, 160, 200, 230, 280, 250, 240, 260, 300, 330],
        "Conversion Rate": [0.10, 0.12, 0.11, 0.13, 0.14, 0.15, 0.16, 0.15, 0.14, 0.15, 0.17, 0.18]
    }
    return pd.DataFrame(data)

df = load_data()

# Title
st.title("Marketing Performance Dashboard")

# Show raw data
st.subheader("Raw Data")
st.dataframe(df)

# KPIs
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

total_sales = df["Sales"].sum()
total_spend = df["Marketing Spend"].sum()
avg_conversion = df["Conversion Rate"].mean()

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Marketing Spend", f"${total_spend:,.0f}")
col3.metric("Avg Conversion Rate", f"{avg_conversion:.2%}")

# Sales vs Marketing Spend Line Chart
st.subheader("Sales vs Marketing Spend Over Time")
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Sales"], marker="o", label="Sales")
ax.plot(df["Month"], df["Marketing Spend"], marker="o", label="Marketing Spend")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.legend()
st.pyplot(fig)

# Leads Generated Bar Chart
st.subheader("Leads Generated")
fig, ax = plt.subplots()
sns.barplot(x="Month", y="Leads Generated", data=df, ax=ax, palette="Blues_d")
st.pyplot(fig)

# Conversion Rate Line Chart
st.subheader("Conversion Rate Over Time")
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Conversion Rate"], marker="o", color="green")
ax.set_xlabel("Month")
ax.set_ylabel("Conversion Rate")
st.pyplot(fig)

