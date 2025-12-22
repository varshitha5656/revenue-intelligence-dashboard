import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Revenue Intelligence Dashboard")
st.write("Simple sales analysis using Python")

# Load data
df = pd.read_csv("data/sales.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Monthly revenue
monthly = (
    df.set_index("OrderDate")
      .resample("M")["Sales"]
      .sum()
      .reset_index()
)

st.subheader("Monthly Revenue Trend")

fig, ax = plt.subplots()
ax.plot(monthly["OrderDate"], monthly["Sales"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Revenue Trend")
st.pyplot(fig)

st.write("Dataset Preview")
st.dataframe(df.head())