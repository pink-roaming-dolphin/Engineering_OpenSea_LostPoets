import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import PIL
import numpy as np


## INTRODUCTORY SALUDOS
st.write('''
### LET THEM HAVE TEA

# 5 p.m. Tea ☕️🍯☕️🥛☕️🍯☕️ 

### It will be you and 2 poets 🐝🐝 ➕ 🐛
### Having tea at the Seaborn Library 🏛️

**These poets have had their genes altered and are mutations of the original LostPoets.* 
A different pair holds a session every week and  every odd day of the week. 
Come join them!**

''')

st.write("When can you make it?")


## GET INPUT FROM USER 
display = ("monday", "wednesday", "friday")
options = list(range(len(display)))
value1 = 1+ st.selectbox("Day of the week", options, format_func=lambda x: display[x])

display = ("1st week", "2nd week", "3rd week", "4th week")
options = list(range(len(display)))
value2 = 1+ st.selectbox("Week of the month", options, format_func=lambda x: display[x])


## USE INPUT TO FIGURE OUT WHICH PATH/IMAGE TO LOAD
poet_pair1 = value1 * value2
poet_pair2 = poet_pair1

path1 = f"generated_images_/{poet_pair1}.png"
path2 = f"generated_images_/{poet_pair2}.png"


##LOAD THE IMAGES IN
poet1 = PIL.Image.open(path1)
poet2 = PIL.Image.open(path1)
st.title("Tea Time!")
for i in range(1, 2):
    cols = st.columns(2)
    cols[0].header("my love")
    cols[0].image(poet1, use_column_width=True)
    cols[1].header("other love")
    cols[1].image(poet2, use_column_width=True)

