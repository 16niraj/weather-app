import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  
import io
import csv  # To save and read data


def get_weather():
    city = city_entry.get().strip()  
    if not city: 
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "90243293f3259202g7684g20"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:  
            weather_desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            icon_code = data["weather"][0]["icon"]  

            
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = Image.open(io.BytesIO(icon_response.content))
            icon_image = ImageTk.PhotoImage(icon_data)
            icon_label.config(image=icon_image)
            icon_label.image = icon_image

            weather_info = (f"Weather: {weather_desc}\nTemperature: {temp}°C\n"
                            f"Humidity: {humidity}%\nWind Speed: {wind_speed} m/s")
            result_label.config(text=weather_info)

            # Save the data
            save_data(city, temp, humidity, wind_speed)

        else:
            error_message = data.get("message", "Unknown error")  # Get the specific error message
            messagebox.showerror("Error", f"City '{city}' not found. Error: {error_message}")
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data!\n{e}")


def save_data(city, temp, humidity, wind_speed):
    file_name = "weather_history.csv"
    data = [city, temp, humidity, wind_speed]

    try:
        with open(file_name, "r", newline="") as file:
            pass  
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Creating a new file.")
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"])  # Header row
        print(f"Header added to {file_name}")

    
    try:
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print(f"Data saved: {data}")
    except Exception as e:
        print(f"Error writing data to file: {e}")



def show_history():
    file_name = "weather_history.csv"
    
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  
            history_text = ""
            for row in reader:
                history_text += f"{row[0]}: {row[1]}°C, {row[2]}% Humidity, {row[3]} m/s\n"

            if history_text:
                history_label.config(text=history_text)
            else:
                history_label.config(text="No past searches found.")
    except FileNotFoundError:
        history_label.config(text="No history available.")

def clear_history():
    try:
        with open("weather_history.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"])  # Reset header
        history_label.config(text="Weather History has been cleared.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clear history: {e}")



# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="#87CEEB")  

# Title
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), bg="#87CEEB")
title_label.pack(pady=10)

# City Input
city_label = tk.Label(root, text="Enter City:", font=("Arial", 12), bg="#87CEEB")
city_label.pack()
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

# Get Weather Button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="blue", fg="white")
get_weather_button.pack(pady=10)

# Weather Icon
icon_label = tk.Label(root, bg="#87CEEB")
icon_label.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#87CEEB")
result_label.pack(pady=10)

# Show History Button
show_history_button = tk.Button(root, text="Show History", command=show_history, font=("Arial", 12), bg="green", fg="white")
show_history_button.pack(pady=10)


# Clear History Button
clear_history_button = tk.Button(root, text="Clear History", command=clear_history, font=("Arial", 12), bg="red", fg="white")
clear_history_button.pack(pady=10)

# History Label
history_label = tk.Label(root, text="", font=("Arial", 10), bg="#87CEEB", justify="left")
history_label.pack(pady=10)

# Run App
root.mainloop()
