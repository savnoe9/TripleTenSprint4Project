# TripleTenSprint4Project

https://tripletensprint4project.onrender.com

This project is designed to perform a basic exploratory data analysis on a dataset, vehicle advertisements in this case.

The dataset used is a file of vehicle advertisement data including vehicle make, model, year, mileage, price and other fields of interest. These fields are used in some analysis to show a scatterplot of price compared to odometer reading at time of sale and vehicle types compared to the number of days that they are listed for.

In this file the libraries used include:

  -pandas
  
  -streamlit
  
  -plotly.figure_factory
  
  -plotly_express
  
  -matplotlib.pyplot
  
  -numpy
  
  -scipy


Methods used in this file include converting columns to appropriate datatypes, dropping rows that are missing important data, adding a new column to comapre luxury vs standard vehicles.

There is a checkbox that allows the selection of data to be viewed to show all vehicles or vehicles listed under $10,000 (a common filter people use when vehicle shopping).

Plotly_express is used to create a histogram and scatterplot and streamlit is used to display these figures in the web app on Render.

To launch this project on your local machine, use git to clone the repository, and navigate to the virtual environment within your terminal. To see the web app, use the command streamlit run app.py within terminal.
