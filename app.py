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

regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

monthly = (
    filtered_df
    .set_index("OrderDate")
    .resample("M")[metric]
    .sum()
    .reset_index()
)

monthly["OrderDate"] = monthly["OrderDate"].astype(str)
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
