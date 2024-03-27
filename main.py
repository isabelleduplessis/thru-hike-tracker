# Required imports
import streamlit as st
import pandas as pd
import datetime
from helpers import percent_completed
from helpers import format_date
from helpers import get_date_today
from helpers import load_hiker_data
from helpers import get_trail_options

### INITIAL PAGE & VARIABLE SET UP ###

# Set page title
st.set_page_config(page_title="Thru-Hike Tracker")

# Load hiker data
hiker_data = load_hiker_data()

# Set start date based on first entry
start_date = hiker_data["Date"].iloc[0]

# Set updated values based on last entry
current_mile = hiker_data["Mile"].iloc[-1]
last_date = hiker_data["Date"].iloc[-1]

# Set trail options based on existing files
trail_names = get_trail_options()[0]
trail_filenames = get_trail_options()[1]


### UDPATE DATA ###

def update_trail_data(trail_selection):
        index = trail_names.index(trail_selection)
        trail_data = trail_filenames[index]
        st.session_state.df = percent_completed(current_mile, trail_data)

def update_hiker_data(date_selection):
        # Keep columns where date <= date_selection
        target_date = start_date - pd.to_timedelta(1, unit='D') + pd.to_timedelta(date_selection, unit='D')
        hiker_data_subset = hiker_data[hiker_data["Date"] <= target_date]
        hiker_data_subset.insert(8, "Formatted Date", hiker_data_subset.loc[:,"Date"].apply(format_date))
        hiker_data_subset = hiker_data_subset[["Formatted Date", "Mile"]].iloc[1: , :]
        hiker_data_subset = hiker_data_subset.rename(columns={"Formatted Date": "Date"})
        st.session_state.hiker_data = hiker_data_subset

### MAIN ###

def main():

        # Create selectbox to choose trail option
        trail_selection = st.selectbox("Select Trail", trail_names)
        
        # Date information
        st.write("Today is ",format_date(get_date_today()))
        st.write("Last update from Isabelle: ", format_date(last_date))
        date_selection = st.slider("Day", 1, (last_date - start_date).days+1)
        
        # Initialize session state variables
        if 'trail_selection' not in st.session_state:
                st.session_state.trail_selection = None
        
        # Update dataframe when selection is changed
        if trail_selection != st.session_state.trail_selection:
                update_trail_data(trail_selection)

        if 'date_selection' not in st.session_state:
                st.session_state.date_selection= None

        if date_selection != st.session_state.date_selection:
                update_hiker_data(date_selection)

        # Initialize df session state variable
        if 'df' not in st.session_state:
                st.session_state.df = percent_completed(current_mile, trail_data)
        
        # Display dataframe
        st.write(st.session_state.df)

        # Display hiker data
        st.write(st.session_state.hiker_data)

if __name__ == "__main__":
    main()

