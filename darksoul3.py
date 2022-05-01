import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Weapon used in dark souls 3 are')
st.subheader('was the tutorial helpful')

weapons=pd.read_csv('https://raw.githubusercontent.com/jeeka7/charts/main/DS3weapon.csv')
st.write(weapons)
pie_chart = px.pie(weapons,
                title='Weapons in the game',
                values='Sell Price',
                names='Name')

st.plotly_chart(pie_chart)
