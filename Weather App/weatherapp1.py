
from tkinter import *
import requests
import json
from datetime import datetime


root = Tk() 
root.title("Weather Application")
root.iconbitmap("/Users/abubakaribrahim/Desktop/Final Project/gui/Tutorial/rose.icns")
root.geometry("420x280")

api_key = "3948361729de2c6601e00639e528f097"




#Function to update weather using new location 
def update():

    # The fields for acces in the functions
    global mylabel1
    global mylabel3
    global mylabel4
    global mylabel5
    global mylabel6

    loc = location.get()
    api_link = "https://api.openweathermap.org/data/2.5/weather?q="+loc+"&appid="+api_key
    api_request = requests.get(api_link)
    api_data = api_request.json()

    if api_data['cod'] == '404':
        # Clearing the fields
        mylabel1.grid_forget()
        mylabel3.grid_forget()
        mylabel4.grid_forget()
        mylabel5.grid_forget()
        mylabel6.grid_forget()

        mylabel = Label(root,text="------------------------------------------------")
        mylabel.grid(row=0,column=0,columnspan=3)
        mylabel1 = Label(root,text="Invalid city Try again!")
        mylabel1.grid(row=1,column=0,columnspan=3)
        mylabe2 = Label(root,text="------------------------------------------------")
    else:
        #create variables to store and display data
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        #Variables for the data to display
        title = "Weather for - {}  || {}".format(loc.upper(), date_time)
        current_temp = "Current temperature is: {:.2f} deg C".format(temp_city)
        weather_discprition = "Current weather desc  : {}".format(weather_desc)
        humidity = "Current Humidity      :  {}  % ".format(hmdt)
        wind_speed = "Current wind speed    : {} kmph".format(wind_spd)

        #clearing the label fields
        mylabel1.grid_forget()
        mylabel3.grid_forget()
        mylabel4.grid_forget()
        mylabel5.grid_forget()
        mylabel6.grid_forget()




        # GUI Design Elements

        mylabel = Label(root,text="------------------------------------------------")
        mylabel.grid(row=0,column=0,columnspan=3)
        mylabel1 = Label(root,text=title)
        mylabel1.grid(row=1,column=0,columnspan=3)
        mylabe2 = Label(root,text="------------------------------------------------")
        mylabe2.grid(row=2,column=0,columnspan=3)
        mylabel3 = Label(root,text=current_temp)
        mylabel3.grid(row=3,column=0,columnspan=3)
        mylabel4 = Label(root,text=weather_discprition)
        mylabel4.grid(row=4,column=0,columnspan=3)
        mylabel5 = Label(root,text=humidity)
        mylabel5.grid(row=5,column=0,columnspan=3)
        mylabel6 = Label(root,text=wind_speed)
        mylabel6.grid(row=6,column=0,columnspan=3)

    



#calling the api request
city ="Ottawa"
api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
api_request = requests.get(api_link)
api_data = api_request.json()






#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#Variables for the data to display
title = "Weather for - {}  || {}".format(city.upper(), date_time)
current_temp = "Current temperature is: {:.2f} deg C".format(temp_city)
weather_discprition = "Current weather desc  : {}".format(weather_desc)
humidity = "Current Humidity      :  {}  % ".format(hmdt)
wind_speed = "Current wind speed    : {} kmph".format(wind_spd)

# GUI Design Elements

mylabel = Label(root,text="------------------------------------------------")
mylabel.grid(row=0,column=0,columnspan=3)
mylabel1 = Label(root,text=title)
mylabel1.grid(row=1,column=0,columnspan=3)
mylabe2 = Label(root,text="------------------------------------------------")
mylabe2.grid(row=2,column=0,columnspan=3)
mylabel3 = Label(root,text=current_temp)
mylabel3.grid(row=3,column=0,columnspan=3)
mylabel4 = Label(root,text=weather_discprition)
mylabel4.grid(row=4,column=0,columnspan=3)
mylabel5 = Label(root,text=humidity)
mylabel5.grid(row=5,column=0,columnspan=3)
mylabel6 = Label(root,text=wind_speed)
mylabel6.grid(row=6,column=0,columnspan=3)

mylabel7 = Label(root,text="Enter new Location")
mylabel7.grid(row=7,column=0)
location = Entry(root,width=30)
location.grid(row=7,column=1)
myButton = Button(root,text="Update",padx=5,pady=5,command=update)
myButton.grid(row=8,column=0,columnspan=3,)


#main loop of the program
root.mainloop()
