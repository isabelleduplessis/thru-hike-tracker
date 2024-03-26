import streamlit as st
st.set_page_config(page_title="Hiker Input Form")

with st.form("date_form"):
	st.write("Hiker Input Form")
	month = st.selectbox("Month", range(1,13)) # eventually make this so that it is autofilled with the current date
	day = st.number_input("Day")
	year = st.number_input("Year")
	mile = st.number_input("Mile Marker")
	location = st.text_input("Location")
	message = st.text_area("Message")
	checkbox_val = st.checkbox("Notify friends & family")
	submit_button = st.form_submit_button("Submit")
# If form is submitted, show the selected date
if submit_button:
	st.success(f"Submitted")
