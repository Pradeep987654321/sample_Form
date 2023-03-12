import streamlit as st
import pandas as pd

st.title("Sample Form")
df=pd.read_csv("data/ss.csv")
st.write(df)

st.sidebar.header("Registration")

sample_form=st.sidebar.form("Form Name")

name=sample_form.text_input("Name")
marks=sample_form.text_input("Marks")
age=sample_form.text_input("Address")

bt=sample_form.form_submit_button()

if bt:
	
	dict1={"Name":name,"Marks":int(marks),"Address":age}
	df=df.append(dict1,ignore_index=True)
	df.to_csv("data/ss.csv",index=False)
