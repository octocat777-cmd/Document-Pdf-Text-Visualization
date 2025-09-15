import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

st.title("📊 User-Driven Data Visualization App")

# Step 0: Data Entry
st.header("📝 Enter Your Data")

# Collect user input
with st.form("data_form"):
    categories = st.text_input("Enter categories (comma-separated)", "A,B,C,D")
    values = st.text_input("Enter values (comma-separated)", "25,35,20,20")
    years = st.text_input("Enter years (comma-separated)", "2020,2021,2022,2023")
    regions = st.text_input("Enter regions (comma-separated)", "North,South,East,West")
    submitted = st.form_submit_button("Submit")

if submitted:
    # Parse input
    cat_list = [x.strip() for x in categories.split(",")]
    val_list = [int(x.strip()) for x in values.split(",")]
    year_list = [int(x.strip()) for x in years.split(",")]
    region_list = [x.strip() for x in regions.split(",")]

    df = pd.DataFrame({
        'Category': cat_list,
        'Value': val_list,
        'Year': year_list,
        'Region': region_list
    })

    # Step 1: Pie Chart
    st.header("Step 1️⃣: 1D Visualization - Pie Chart")
    fig1, ax1 = plt.subplots()
    ax1.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Step 2: Line Graph
    st.header("Step 2️⃣: 2D Visualization - Line Graph")
    fig2, ax2 = plt.subplots()
    ax2.plot(df['Year'], df['Value'], marker='o')
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Value")
    ax2.set_title("Value over Time")
    st.pyplot(fig2)

    # Step 3: Mosaic Plot
    st.header("Step 3️⃣: Multi-Dimensional Visualization - Mosaic Plot")
    mosaic_df = pd.DataFrame({
        'Category': cat_list * 2,
        'Region': region_list * 2,
        'Count': val_list + val_list[::-1]
    })
    mosaic_data = mosaic_df.groupby(['Category', 'Region'])['Count'].sum().to_dict()
    fig3, _ = mosaic(mosaic_data, title='Category vs Region Mosaic Plot')
    st.pyplot(fig3)
