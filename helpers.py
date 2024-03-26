import pandas as pd
import datetime
from datetime import date

### DATES ###

# Function to get date from entered year, month, ada
def get_date_from_entry(year, month, day):
        x = date(year, month, day)
        return x

# Function to get current_date
def get_date_today():
        today = date.today()
        return today

# Function to initialize start date
def initialize_start_date(year, month, day):
        start_date = datetime.date(year, month, day)
        return start_date

# Function to get day number
def get_day_number(start_date, today = get_date_today()):
        return (today - start_date)

# Function to format date for printing
def format_date(date):
        return date.strftime("%B %d, %Y")

current_date = format_date(get_date_today())
num_days = get_day_number(initialize_start_date(2023,12,23)).days

#print(current_date)
#print("Day ", num_days)

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
