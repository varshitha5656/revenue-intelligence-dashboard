import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Revenue Intelligence Dashboard")
st.write("Simple sales analysis using Python")

# Load data
df = pd.read_csv("data/sales.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Profit"] = df["Sales"] - df["Cost"]
metric = st.radio(
    "Select Metric",
    ["Sales", "Profit"],
    horizontal=True
)
st.sidebar.header("Filters")

categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

if selected_category != "All":
    df = df[df["Category"] == selected_category]
    regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

if selected_region != "All":
    df = df[df["Region"] == selected_region]
# Monthly revenue
monthly = (
    df.groupby(df["OrderDate"].dt.to_period("M"))[metric]
      .sum()
      .reset_index()
)

col1, col2 = st.columns(2)

col1.metric(
    label=f"Total {metric}",
    value=f"{df[metric].sum():,.0f}"
)

col2.metric(
    label="Total Orders",
    value=df.shape[0]
)
st.subheader("Monthly Revenue Trend")

fig, ax = plt.subplots()

ax.plot(
    monthly["OrderDate"].astype(str),
    monthly[metric],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel(metric)
ax.set_title(f"Monthly {metric} Trend")

st.pyplot(fig)
st.write("Dataset Preview")
st.dataframe(df.head())