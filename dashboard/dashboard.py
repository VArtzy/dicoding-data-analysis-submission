import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

df = pd.read_csv('dashboard/main_data.csv')

st.title('Bike Sharing Dashboard')

datetime_column = 'dteday'
df.sort_values(datetime_column, inplace=True)
df.reset_index(inplace=True)
df[datetime_column] = pd.to_datetime(df[datetime_column])

min_date = df[datetime_column].min()
max_date = df[datetime_column].max()

with st.sidebar:
    st.image('https://www.pngplay.com/wp-content/uploads/6/Downhill-Bike-Vector-PNG-Clipart-Background.png')

    start_date = st.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input('End date', max_date, min_value=min_date, max_value=max_date)

main_df = df[(df[datetime_column] >= str(start_date)) & (df[datetime_column] <= str(end_date))]

st.subheader("Rides by Temperature")
 
fig, ax = plt.subplots(figsize=(20, 10))

plt.bar(x=main_df["cuaca"], height=main_df["cnt"])

ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Temparature vs Rides")

fig, ax = plt.subplots(figsize=(20, 10))

sns.regplot(x=main_df["temp"] * 41, y=main_df["cnt"])
plt.xlabel("Temperatur (dalam celcius)")
plt.ylabel("Jumlah perental sepeda")
st.pyplot(fig)

st.subheader("Rides by Season")
 
fig, ax = plt.subplots(figsize=(20, 10))

plt.bar(x=main_df["season"], height=main_df["cnt"])

ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
