import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import PIL
import numpy as np


st.markdown(
    """
 <style>
.stApp {
  background-image: url("https://htmlcolorcodes.com/assets/images/colors/turquoise-color-solid-background-1920x1080.png");
  background-size: cover;
}
</style>
    """,
    unsafe_allow_html=True
)


####################################
######INTRODUCTORY SALUDOS##########
####################################

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

####################################
####GET INPUT FROM USER#############
####################################

display = ("choose a day", "monday", "wednesday", "friday")
options = list(range(len(display)))
value1 = st.selectbox("Day of the week", options, format_func=lambda x: display[x])

display = ("choose a week", "1st week", "2nd week", "3rd week", "4th week")
options = list(range(len(display)))
value2 = st.selectbox("Week of the month", options, format_func=lambda x: display[x])


######################################################
##USE INPUT TO FIGURE OUT WHICH PATH/IMAGE TO LOAD####
######################################################
    ####################################
    ######## & LOAD IMAGES IN###########
    ####################################

# if only prompt, then do nothing 
# otherwise load images in: 
   
if (value1 != 0) & (value2 != 0):
    poet_pair1 = value1 * value2
    poet_pair2 = poet_pair1 + 1

    path1 = f"generated_images/{poet_pair1}.png"
    path2 = f"generated_images/{poet_pair2}.png"


    poet1 = PIL.Image.open(path1)
    poet2 = PIL.Image.open(path2)
    st.title("Tea Time!")
    for i in range(1, 2):
        cols = st.columns(2)
        cols[0].header("Left Chair Poet")
        cols[0].image(poet1, use_column_width=True)
        cols[1].header("Right Chair Poet")
        cols[1].image(poet2, use_column_width=True)


####################################
#########CREDITS####################
####################################
st.write("*[LostPoets on OpenSea](https://opensea.io/collection/lostpoets)")
