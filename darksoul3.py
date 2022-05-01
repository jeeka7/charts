import pandas as pd
import streamlit as st
#import plotly.express as px
#from PIL import Image

st.set_page_config(page_title='Dark Souls 3 weapon')
st.header('Weapon used in dark souls 3 are')
st.subheader('was the tutorial helpful')

weapons=pd.read_csv("https://raw.githubusercontent.com/jeeka7/charts/main/DS3weapon.csv")
print(weapons)
