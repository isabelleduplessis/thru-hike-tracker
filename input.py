import streamlit as st

with st.form("my_form"):
	st.write("Inside the form")
	slider_val = st.slider("Form slider")
	checkbox_val = st.checkbox("Notify Friends & Family")

	submitted = st.form_submit_button("Submit")
	if submitted:
		st.write("slider", slider_val, "checkbox", checkbox_val)

	st.write("outside the form")
