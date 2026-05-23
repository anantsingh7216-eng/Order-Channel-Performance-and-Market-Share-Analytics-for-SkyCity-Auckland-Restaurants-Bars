import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Channel Analytics Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\Danish\Downloads\SkyCity Auckland Restaurants & Bars.csv")

df = load_data()

st.title("📊 SkyCity Auckland Channel Performance Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")

subregion = st.sidebar.multiselect(
    "Select Subregion",
    options=df["Subregion"].unique(),
    default=df["Subregion"].unique()
)

cuisine = st.sidebar.multiselect(
    "Select Cuisine",
    options=df["CuisineType"].unique(),
    default=df["CuisineType"].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    (df["Subregion"].isin(subregion)) &
    (df["CuisineType"].isin(cuisine)) &
    (df["Segment"].isin(segment))
]

# -----------------------------
# Channel Market Share
# -----------------------------
st.subheader("📌 Channel Market Share")

channel_data = pd.DataFrame({
    "Channel": ["InStore", "UberEats", "DoorDash", "SelfDelivery"],
    "Orders": [
        filtered_df["InStoreOrders"].sum(),
        filtered_df["UberEatsOrders"].sum(),
        filtered_df["DoorDashOrders"].sum(),
        filtered_df["SelfDeliveryOrders"].sum()
    ]
})

fig = px.pie(channel_data, names="Channel", values="Orders", title="Market Share")
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Subregion Heatmap
# -----------------------------
st.subheader("🌍 Subregion Channel Distribution")

subregion_data = filtered_df.groupby("Subregion")[[
    "InStoreOrders",
    "UberEatsOrders",
    "DoorDashOrders",
    "SelfDeliveryOrders"
]].sum().reset_index()

fig2 = px.bar(
    subregion_data,
    x="Subregion",
    y=subregion_data.columns[1:],
    title="Channel Orders by Subregion",
    barmode="stack"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Cuisine vs Channel
# -----------------------------
st.subheader("🍔 Cuisine Channel Mix")

cuisine_data = filtered_df.groupby("CuisineType")[[
    "InStoreOrders",
    "UberEatsOrders",
    "DoorDashOrders",
    "SelfDeliveryOrders"
]].mean().reset_index()

fig3 = px.bar(
    cuisine_data,
    x="CuisineType",
    y=cuisine_data.columns[1:],
    title="Average Channel Orders by Cuisine",
    barmode="group"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Dependency Risk
# -----------------------------
st.subheader("⚠️ Dependency Risk")

filtered_df["AggregatorDependence"] = (
    filtered_df["UE_share"] + filtered_df["DD_share"]
)

high_risk = filtered_df[filtered_df["AggregatorDependence"] > 0.7]

st.metric("High Risk Restaurants", len(high_risk))

st.dataframe(high_risk[[
    "RestaurantName",
    "Subregion",
    "CuisineType",
    "AggregatorDependence"
]])

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📈 Key KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", int(filtered_df["MonthlyOrders"].sum()))
col2.metric("Avg Order Value", round(filtered_df["AOV"].mean(), 2))
col3.metric("Avg Growth", round(filtered_df["GrowthFactor"].mean(), 3))