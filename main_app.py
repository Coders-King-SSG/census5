import numpy as np
import pandas as pd
import data
import plot
import streamlit as st

@st.cache()
def load_data():
	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 
               'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)
	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)
	df.dropna(inplace=True)
	df.drop(columns='fnlwgt',axis=1,inplace=True)
	return df
st.set_option('deprecation.showPyplotGlobalUse', False)
df = load_data()

	
	# Adding a navigation in the sidebar using radio buttons
# Create a dictionary.
pages_dict = {"View Data": data, "Visualise Data": plot}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
selected_page = pages_dict[user_choice]
selected_page.app(df) 
