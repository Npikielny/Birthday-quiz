"""
birthday.py
Author: Noah Pikielny
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
#setup
from datetime import datetime
from calendar import month_name
from math import ceil
todayMonth = datetime.today().month
monthIndex = {1 : "january", 2 : "february", 3 : "march", 4 : "april", 5 : "may", 6 : "june",7 : "july", 8 : "august", 9 : "september", 10 : "october", 11 : "november", 12 : "december"}
todayDay = datetime.today().day
todayYear= datetime.today().year

#inputs
name = str(input("Hello, what's your name?"))
month = input("Hi " + name + ", what was the name of the month were you born in?")
year = input("And what year you were born in, " + name + " ?")
day = input("And what day?")

#Analyzing data
responses = 0
decades = {1 : "stone age", 2 : "eighties", 3 : "nineties", 4 : "two thousands"}
season = ""
decade = ""

#-----#Determining season of birth
if month.lower() == "december" or month.lower() == "january" or month.lower() == "february":
    season = "winter"
elif month.lower() == "march" or month.lower() == "april" or month.lower() == "may":
    season = "spring"
elif month.lower() == "june" or month.lower() == "july" or month.lower() == "august":
    season = "summer"
elif month.lower() == "september" or month.lower() == "november" or month.lower() == "october":
    season = "fall"

#-----#Determining Decade in which the user was born
if int(year) < 1980:
    decade = decades[1]
else:
    decade = ceil((int(year) + 1 - 1980) / 10) + 1

#Output
if month.lower() == monthIndex[todayMonth] and int(day) == todayDay:
    print("Happy Birthday!")
    responses += 1
if month.lower() == "october" and int(day) == 31:
    print("You were born on Halloween!")
    responses += 1
if responses == 0:
    print(str(name) + ", you are a " + season + " baby of the " + str(decades[decade]) + ".")
