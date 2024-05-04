import tkinter as tk
from tkinter import messagebox
import requests

def fetch_weather():
    city = city_entry.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    try:
        # Fetch weather data in Fahrenheit
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        weather_data.raise_for_status()  # Raise an exception for any HTTP error
        weather_json = weather_data.json()
        if weather_json.get('cod') == 200:
            weather_fahrenheit = weather_json['weather'][0]['main']
            temp_fahrenheit = round(weather_json['main']['temp'])
            # Convert temperature to Celsius
            temp_celsius = round((temp_fahrenheit - 32) * 5/9)
            result_label.config(text=f"The weather in {city} is: {weather_fahrenheit}\nTemperature (F): {temp_fahrenheit}ºF\nTemperature (C): {temp_celsius}ºC")
        else:
            messagebox.showerror("Error", "City not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
city_label = tk.Label(root, text="Enter city:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()