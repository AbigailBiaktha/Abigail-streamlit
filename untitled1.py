# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 18:10:27 2023

@author: Lenovo
"""

import streamlit as st
import pandas as pd
st.write("My First Stremlit app")
data={"sales":[30,40,50,20,10,40]}
df=pd.DataFrame(data)
st.line_chart(df)

