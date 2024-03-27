# Required imports
import streamlit as st
import pandas as pd
import datetime
from helpers import percent_completed
from helpers import format_date
from helpers import get_date_today
from helpers import load_hiker_data
from helpers import get_trail_names
from helpers import get_trail_filenames
from helpers import update_trail_data


### INITIAL PAGE & VARIABLE SET UP ###

# Set page title
st.set_page_config(page_title="Thru-Hike Tracker")

#user_name = "sample_hiker_data"


# need to make hiker data change based on trail selection


### UDPATE DATA ###




### MAIN ###

# session state variables - date selection, trail selection


def main():
        st.title("Thru-Hike Tracker")

        # Date information
        st.write("Today is ",format_date(get_date_today()))
        #st.write("Last update from Isabelle: ", format_date(last_date))

        ### SELECTBOX ### this works

        # Initialize selected session state variables
        if 'trail_selection' not in st.session_state:
                st.session_state.trail_selection = None

        # Create selectbox to choose trail option
        user_name = "sample_hiker_data"
        trail_selection = st.selectbox("Select Trail", get_trail_names(user_name))
        
        # Update page when selection is changed
        if trail_selection != st.session_state.trail_selection:
                update_trail_data(user_name, trail_selection)
        
        ### PROGRESS DATAFRAME & HIKER DATA ###

        # Initialize displayed session state variables
        if 'df' not in st.session_state:
                st.session_state.df = percent_completed(current_mile, trail_data)
        
        # Display dataframe
        st.write(st.session_state.df)


        # Display hiker data
        st.write(st.session_state.hiker_data)

if __name__ == "__main__":
    main()

