import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title='Census | Main', page_icon='logo.png', layout='centered', initial_sidebar_state='auto')
st.set_option('deprecation.showPyplotGlobalUse', False)
def app(df):
	opt = ('Boxplot', 'Piechart', 'Countplot', 'Scatterplot', 'Regplot', 'Linegraph')
	grp = st.selectbox('Select the graph/chart/plot you want to view', opt)
	col = st.selectbox('Select column', df.columns)
	st.write('Please choose a numerical value else you\'d receive an error!')
	if st.button('Display'):
		if grp == opt[0]:
			plt.figure(figsize=(10,5))
			sns.boxplot(df[col])
			st.pyplot()
		if grp == opt[1]:
			plt.figure(figsize=(5,5))
			plt.pie(df[col].value_counts(), labels=df[col].value_counts().index, autopct='%.2f')
			st.pyplot()
		if grp == opt[2]:
			plt.figure(figsize=(15,5))
			sns.countplot(df[col])
			st.pyplot()
		if grp == opt[3]:
			y = st.selectbox('Select column for y-axis', df.columns)
			plt.figure(figsize=(15,5))
			plt.scatter(df[col], df[y])
			st.pyplot()
		if grp == opt[4]:
			plt.figure(figsize=(15,5))
			sns.regplot(df[col])
			st.pyplot()
		if grp == opt[5]:
			y = st.selectbox('Select column for y-axis', df.columns)
			plt.figure(figsize=(15,5))
			plt.plot(df[col], df[y])
			st.pyplot()