import pandas as pd
import datetime
from datetime import date
import glob


### LOADING DATA ###
def load_hiker_data():
        # Read in user data
        hiker_data = pd.read_csv("sample_hiker_data.csv")
        # Create column with datetime values
        hiker_data.insert(7, "Date", pd.to_datetime(hiker_data[["Year", "Month", "Day"]]))
        # TODO: sort by date and remove redundant columns
        return hiker_data

def get_trail_options():
        # Read in all files in trail_data to get list of trails as options for the selectbox
        trail_files = glob.glob("trail_data/*.csv")

        # Create empty lists
        trail_names = []
        trail_filenames = []

        # Add each trail name and file name to lists
        for file in trail_files:
                df = pd.read_csv(file)
                trail_names.append(df.iloc[0,-1])
                trail_filenames.append(file)
        return [trail_names, trail_filenames]

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

  
