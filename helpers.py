import streamlit as st
import pandas as pd
import datetime
from datetime import date
import glob

def update_trail_data(user_name, trail_selection):
        trail_names = get_trail_names(user_name)
        trail_filenames = get_trail_filenames(user_name)
        index = trail_names.index(trail_selection)
        trail_data = trail_filenames[index]
        # Once trail has been selected, load hiker data
        hiker_data = load_hiker_data(user_name, trail_selection)
        # Set start date based on first entry
        start_date = hiker_data["Date"].iloc[0]
        # Set updated values based on last entry
        current_mile = hiker_data["Mile"].iloc[-1]
        last_date = hiker_data["Date"].iloc[-1]
        st.session_state.df = percent_completed(current_mile, trail_data)
        st.session_state.hiker_data = hiker_data

### LOADING DATA ###

def get_trail_names(user_name): # Get the trails that a user has data on to select which trail data to view
        dir_name = user_name + "/*.csv"
        user_files = glob.glob(dir_name) # Locate directory that belongs to the user
        trail_names = []
        #trail_filenames = []
        for file in user_files:
                df = pd.read_csv(file)
                trail_names.append(df["Trail"].iloc[0])
        return trail_names

def get_trail_filenames(user_name):
        trail_filenames = []
        for trail in get_trail_names(user_name):
                for file in glob.glob("trail_data/*.csv"):
                        df = pd.read_csv(file)
                        if trail == df["Trail"].iloc[0]:
                                trail_filenames.append(file)
        return trail_filenames


def load_hiker_data(user_name, trail_name): # Use load_hiker_data("sample_hiker_data", "Colorado Trail")
        # Read in user data
        dir_name = user_name + "/*.csv"
        user_files = glob.glob(dir_name) # Locate directory that belongs to the user
        for file in user_files:
                df = pd.read_csv(file)
                if df["Trail"].iloc[0] == trail_name:
                        hiker_data = df
        # Create column with datetime values
        hiker_data.insert(7, "Date", pd.to_datetime(hiker_data[["Year", "Month", "Day"]]))
        # TODO: sort by date and remove redundant columns
        return hiker_data


# Will only be used in hiker input file
def get_trail_options(): # Get the trails that exist in the system to allow the hiker to choose from
        #Read in all files in trail_data to get list of trails as options for the selectbox
        trail_files = glob.glob("trail_data/*.csv")
        # Create empty lists
        trail_names = []
        #trail_filenames = []
        # Add each trail name and file name to lists
        for file in trail_files:
                df = pd.read_csv(file)
                trail_names.append(df["Trail"].iloc[0])
                #trail_filenames.append(file)
        return trail_names

### DATES ###

# Function to get current_date
def get_date_today():
        today = date.today()
        return today

# Function to format date for printing
def format_date(date):
        return date.strftime("%B %d, %Y")


### SECTION INFO ###

def get_section_list(trail_data):
        df = pd.read_csv(trail_data)
        return df.iloc[:, 0].unique()

def get_mile_list(trail_data):
        df = pd.read_csv(trail_data)
        mile_list = [0]
        # subset df to only include first entry in section list
        for section in get_section_list(trail_data):
                tmpdf = df.loc[df["Section"] == section]
                mile_list.append(tmpdf["Mile"].iloc[-1])
        return mile_list

### MILES COMPLETED ###

def percent_completed(current_mile, trail_data):
        df = pd.DataFrame(columns=["Section", "Total Miles", "Completed Miles", "Percent Complete"], dtype='string')
        section_list = get_section_list(trail_data)
        mile_list = get_mile_list(trail_data)
        for i in range(0,len(section_list)):
                section = section_list[i]
                percent_complete = 0
                # append percentage to dataframe for each section
                section_length = mile_list[i+1] - mile_list[i]
                completed_miles = current_mile - mile_list[i]
                if completed_miles < 0:
                        completed_miles = 0
                if completed_miles > section_length:
                        completed_miles = section_length
                percent_complete = completed_miles/section_length
                new_row = {"Section": section, "Total Miles": section_length, "Completed Miles": completed_miles, "Percent Complete": percent_complete}
                df = pd.concat([df if not df.empty else None, pd.DataFrame([new_row])], ignore_index=True)
        df["Percent Complete"] = df["Percent Complete"].map('{:.1%}'.format)
        return df    

  
