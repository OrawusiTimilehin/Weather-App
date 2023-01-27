# Weather-App


#Overview
This is a simple weather App which uses the TKinter Gui Package and allows for user interaction. It takes in the name of
a city, carries out analysis on the city's current time, sunset time, sunrise time, time-zone id, weather conditions
from the Api in order to deliver a beautifully designed user interface that displays the time, date, city name ,
Image depicting the current weather and also the images for the weather forecast for various hours of the day.
This program does not have to be run each time when you want to select a new City as it contains a user interface to go
back and re-select a City.


#Skills -

APIs
OOP - Object-Oriented Programming
Tkinter
Data Structures
Modularization of Code
Programming Logic and basic concepts
Flow Structures

#Code Structure -
This Program is written using Object-Oriented Programming and has two modules -

1. main.py
2. brain.py

#Main.py -
This module contains the main flow of the program, contains the initialisation of class objects and tkinter object and
contains the tkinter structure, frames, widgets and the code
for its layout on the screen.

The frames are loaded into the window, the frist frame is programmed to show first - hence the initialisation of the
"load_frame1" method. Frame 1 contains a user entry in which the user is to type in the "City" of choice. This city is
then passed into the "get_city" which populates the Data class attributes. After all the data processing, Frame 2
displays all the information
and images and a button inorder the go back to re-select the City.


#Brain.py -
This module contains the Data class , which contains the various methods that request data from the APIs and populates
the Data class attributes. The class also contains a method that contains the decision system which determines the
images displayed based on the data and time in the city. This method checks if the condition returned from the Api is in
the weather conditions dictionary which has the conditions as keys and the image directories as values.
If it is in the dictionary it returns the images path associated with that weather condition



#APIs
Powered by WeatherAPI.com - https://www.weatherapi.com/
Powered by  Ipgeolocation.com - https://ipgeolocation.io/

#Libraries and Packages and Imports
Tkinter
PIL
requests


