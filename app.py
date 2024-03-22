# Import required packages
import streamlit as st
import pandas as pd
import datetime

# Function to initialize DataFrame
def initialize_dataframe():
	return pd.DataFrame(columns=["Date", "Mile", "Day"])

# Function to get date
def get_date(year, month, day):
	x = datetime.datetime(year, month, day)
	return x.strftime("%x")

# Function to update DataFrame
def update_df(date, mile):
	df = df.append({"Date": date, "Mile": mile})
	return df

# Function to calculate day number

# Function to input start date

# Initialize section list
section_list = ["Southern California", "Sierra Nevada", "Northern California", "Oregon", "Washignton"]
mile_list = [0, 703.4, 1093.4, 1719.7, 2155.0, 2652.6]


	

# Function to calcuate % of hike completed
def percent_completed(current_mile, section_list, mile_list):
	df = pd.DataFrame(columns=["Section", "Total Miles", "Completed Miles", "Percent Complete"])
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
		df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
	df["Percent Complete"] = df["Percent Complete"].map('{:.1%}'.format)
	return df


def main():
	# Set app title
	st.title("PCT Progress")

	# Take current mile as input
	#current_mile = int(st.text_input("Enter current mile:", ''))

	# Initialize or load the DataFrame
	if 'df' not in st.session_state:
		st.session_state.df = percent_completed(0, section_list, mile_list)
	st.write(st.session_state.df)

if __name__ == "__main__":
	main()
