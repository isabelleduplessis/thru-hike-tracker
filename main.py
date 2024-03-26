import streamlit as st
import pandas as pd
from helpers import percent_completed
from helpers import format_date
from helpers import get_date_today
import datetime

st.set_page_config(page_title="Thru-Hike Tracker")

# Initialize section list
#section_list = ["Southern California", "Sierra Nevada", "Northern California", "Oregon", "Washignton"] # generate section and mile list by gettin gend values of each section from trail data
#mile_list = [0, 703.4, 1093.4, 1719.7, 2155.0, 2652.6]

trail_options = ["Colorado Trail", "Pacific Crest Trail"] # have it get unique trail names from trail data folder
hiker_data = pd.read_csv("sample_hiker_data.csv")
hiker_data.insert(6, "Date", pd.to_datetime(hiker_data[["Year", "Month", "Day"]]))
# sort by date and remove redundant columns
current_mile = hiker_data["Mile"].iloc[-1]
start_date = hiker_data["Date"].iloc[0]
last_date = hiker_data["Date"].iloc[-1]
hiker_data_subset = hiker_data
target_date = last_date


def update_trail_data(trail_selection):
        if trail_selection == "Pacific Crest Trail":
                        # Update dataframe with pct trail data
                        trail_data = "trail_data/pct.csv"
        elif trail_selection == "Colorado Trail":
                        # Update dataframe with ct trail data
                        trail_data = "trail_data/ct.csv"
        st.session_state.df = percent_completed(current_mile, trail_data)

def update_hiker_data(date_selection):
        # Keep columns where date <= date_selection
        target_date = start_date - pd.to_timedelta(1, unit='D') + pd.to_timedelta(date_selection, unit='D')
        hiker_data_subset = hiker_data[hiker_data["Date"] <= target_date]
        hiker_data_subset["Date"] = hiker_data_subset["Date"].apply(format_date)
        hiker_data_subset = hiker_data_subset[["Date", "Mile"]].iloc[1: , :]
        st.session_state.hiker_data = hiker_data_subset

def main():
        # Create selectbox to choose trail option
        trail_selection = st.selectbox("Select Trail", trail_options)
        
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

        st.write(format_date(target_date))

        # Display hiker data
        st.write(st.session_state.hiker_data)

if __name__ == "__main__":
    main()

