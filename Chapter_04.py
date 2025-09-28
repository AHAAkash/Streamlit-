import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

file  = st.file_uploader("UPload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)

if file:
    st.subheader("Sales Over Time")
    df["Date"] = pd.to_datetime(df["Date"])
    sales_over_time = df.groupby("Date")["Revenue"].sum().reset_index()
    st.line_chart(sales_over_time.set_index("Date"))
    st.bar_chart(sales_over_time.set_index("Date"))
    st.area_chart(sales_over_time.set_index("Date"))
    st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")