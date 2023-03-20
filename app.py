import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title='Price Tracking Data Visualization and Analysis')

# Load data
data = pd.read_csv('price_data.csv')

# Sidebar options
st.sidebar.title('Options')
selected_product = st.sidebar.selectbox('Select Product', sorted(data['product_name'].unique()))
selected_date = st.sidebar.slider('Select Date Range', min_value=data['date'].min(), max_value=data['date'].max(), value=(data['date'].min(), data['date'].max()))

# Filter data
filtered_data = data[(data['product_name']==selected_product) & (data['date']>=selected_date[0]) & (data['date']<=selected_date[1])]

# Show data
st.write(f"Showing data for '{selected_product}' from {selected_date[0]} to {selected_date[1]}")
st.write(filtered_data)

# Price distribution plot
fig1, ax1 = plt.subplots()
sns.histplot(data=filtered_data, x='price', kde=True, ax=ax1)
ax1.set_title(f'Distribution of Prices for {selected_product}')
st.pyplot(fig1)

# Price over time plot
fig2, ax2 = plt.subplots()
sns.lineplot(data=filtered_data, x='date', y='price', ax=ax2)
ax2.set_title(f'Price Trend for {selected_product}')
st.pyplot(fig2)