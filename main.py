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
current_mile = 50

hiker_data = pd.read_csv("sample_hiker_data.csv")
start_date = datetime.date(hiker_data["Year"].iloc[0], hiker_data["Month"].iloc[0], hiker_data["Day"].iloc[0])
last_date = datetime.date(hiker_data["Year"].iloc[-1], hiker_data["Month"].iloc[-1], hiker_data["Day"].iloc[-1])

def update_data(trail_selection):
        if trail_selection == "Pacific Crest Trail":
                        # Update dataframe with pct trail data
                        trail_data = "trail_data/pct.csv"
        elif trail_selection == "Colorado Trail":
                        # Update dataframe with ct trail data
                        trail_data = "trail_data/ct.csv"
        st.session_state.df = percent_completed(current_mile, trail_data)

def main():
        # Create selectbox to choose trail option
        trail_selection = st.selectbox("Select Trail", trail_options)
        
        # Initialize session state variables
        if 'trail_selection' not in st.session_state:
                st.session_state.trail_selection = None
        
        
        # Update dataframe when selection is changed
        if trail_selection != st.session_state.trail_selection:
                update_data(trail_selection)
                #st.session_state.trail_selection

        # Date information
        st.write("Today is ",format_date(get_date_today()))
        st.write("Last update from Isabelle: ", format_date(last_date))
        selected_date = st.slider("Day", 1, (last_date - start_date).days+1)
        st.write(format_date(start_date - pd.to_timedelta(1, unit='D') + pd.to_timedelta(selected_date, unit='D')))

        # Initialize df session state variable
        if 'df' not in st.session_state:
                st.session_state.df = percent_completed(current_mile, trail_data)
        
        # Display dataframe
        st.write(st.session_state.df)

if __name__ == "__main__":
    main()

