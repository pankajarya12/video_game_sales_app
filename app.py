import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

st.title("🎮 Video Game Sales Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("vgsales.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")

platform = st.sidebar.multiselect(
    "Select Platform",
    options=df["Platform"].unique(),
    default=df["Platform"].unique()
)

genre = st.sidebar.multiselect(
    "Select Genre",
    options=df["Genre"].unique(),
    default=df["Genre"].unique()
)

filtered_df = df[(df["Platform"].isin(platform)) & (df["Genre"].isin(genre))]

# Show Data
st.subheader("📊 Dataset Overview")
st.write(filtered_df.head())

st.write("Total Games:", filtered_df.shape[0])

# Sales by Platform
st.subheader("💻 Global Sales by Platform")
platform_sales = filtered_df.groupby("Platform")["Global_Sales"].sum().sort_values()

fig1, ax1 = plt.subplots()
platform_sales.plot(kind="barh", ax=ax1)
ax1.set_xlabel("Global Sales (Millions)")
ax1.set_ylabel("Platform")
st.pyplot(fig1)

# Sales by Genre
st.subheader("🎯 Global Sales by Genre")
genre_sales = filtered_df.groupby("Genre")["Global_Sales"].sum()

fig2, ax2 = plt.subplots()
genre_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# Top 10 Games
st.subheader("🏆 Top 10 Games by Global Sales")
top_games = filtered_df.sort_values("Global_Sales", ascending=False).head(10)

fig3, ax3 = plt.subplots()
ax3.barh(top_games["Name"], top_games["Global_Sales"])
ax3.set_xlabel("Global Sales (Millions)")
ax3.invert_yaxis()
st.pyplot(fig3)

st.success("Dashboard Loaded Successfully 🚀")
