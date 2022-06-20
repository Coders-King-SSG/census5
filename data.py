import numpy as np
import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
def app(df):
	st.header('Census Data')
	st.write('This app will help you to visualize the census data\n\n')
	with st.expander('View Data'):
		st.table(df.head())
	c1, c2 = st.columns(2)
	with c1:
		if st.checkbox('Show column names'):
			st.table(df.columns)
	with c2:
		if st.checkbox('Show data description'):
			st.table(df.describe())
	c3, c4 = st.columns(2)
	with c3:
		if st.checkbox('Show column data-types'):
			st.write(df[st.selectbox('Select column',df.columns)].dtype)
	with c4:
		if st.checkbox('Show column data'):
			st.table(df[st.selectbox('Select column',df.columns)].value_counts())
