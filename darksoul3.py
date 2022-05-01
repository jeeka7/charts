import pandas as pd
import streamlit as st

st.header('Weapon used in dark souls 3 are')
st.subheader('was the tutorial helpful')

weapons=pd.read_csv('https://raw.githubusercontent.com/jeeka7/charts/main/DS3weapon.csv')
print(weapons)
