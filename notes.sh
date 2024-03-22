#!/bin/bash

#code i've typed

pip install streamlit
pip install watchdog

mkdir streamlit_app
cd streamlit_app


streamlit run app.py

vi requirements.txt
# include name of all python packages used


#https://towardsdatascience.com/3-easy-ways-to-deploy-your-streamlit-web-app-online-7c88bb1024b1

#4.1. Set up a Streamlit Cloud Account
#Create a Streamlit cloud account here: https://streamlit.io/cloud

#4.2. Create a New App and Link your GitHub Account
#Once you are logged in, there should be a very obvious (you’ll see why) ‘New app’ button for you to click on.
#You will then see a prompt to ‘Connect to GitHub’. Log in to the GitHub account that you created earlier.
#4.3. Deploy your App
#In the next screen, search for your GitHub repository that you created earlier by typing its name under ‘Repository’.
#Change the ‘Main file path’ to ‘app.py’.
#Click on Deploy!


#Things I want to do with this app

#Display table showing 
	#Section, Town, PCT Mile #, Schedule, Day #, Direction




#Information that I'll input:
	#current date
	#current mile




#Enter towns and corresponding mileage
#have it figure out what section the town is in
#have this as a csv file


#make a table with town, mileage, and coordinates


#estimated arrival
	#have avg pace for 4.5 and 5 months
	#calculate based on start date



#it would be cool if i could show coordinates on a map that then link to the date I got there, a description, and pictures


echo "# thru-hike-tracker" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/isabelleduplessis/thru-hike-tracker.git
git push -u origin main

#make it so that it removes any duplicate rows in hiker_data.csv

#Hiker page
#select what trail being hiked
#submit new mileage
#view and edit friends and family email list


#Friends & family page


#https://docs.streamlit.io/streamlit-community-cloud/share-your-app




