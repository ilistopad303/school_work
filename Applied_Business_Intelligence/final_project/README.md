# Ian Listopad Final Project

## File Structure
Python Script: final.py, This is where most of the data is cleaned and went through. This outputs a new cleaned_CSV.csv file.  
Power BI: Final Project.pbix, This is my PowerBI dashboard file that helps show the overall trends of the data. This uses the cleaned_CSV.csv file from the Python script.  
DataSet: Historical State Residency per year.csv, This is my original csv dataset I got from teh Census Bureau showing all the residency information from 1910 to 2020  
DataSet: Cleaned_CSV.csv, This is the cleaned up dataset output from my python script  
Readme: README.md, This is the file that I am writing in to show all of the other files and walkthrough how they should be used.  
Report: Final Project Report.docx, This is my Report with all my analysis and more in depth of the process that I took.  

## Project Walkthrough
My Project should start with the Python Script final.py. This will prompt you for the year range you would like to see data from. Input the starting year first
and the end year second.
This then does all of the data preparation such as dropping the columns that are not relevant to my question as well as helping with changing and reformatting 
columns to be able to use later in the script. It will also create one linechart to show the overall trend of population from the start year you entered to the ending year,
and print a new data table showing the overall percent change between the beginning year and the ending year. 

This can then be paired with the Power BI Dashboard to see some more visuals of this data including a bar chart, pie chart, and Sankey chart. The pie chart and bar chart
help users visualize the percent change year over year. Filter for one year and that will allow users to interactively see the change for each state for that year.
The Sankey Chart helps show the distribution of the total United States population for that year, It is useful to show where the concentration of population is within the United states.


