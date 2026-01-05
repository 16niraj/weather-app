# Weather App using Python (Tkinter)

## 📌 Project Overview

This project is a **GUI-based Weather Application** developed using **Python and Tkinter**. It allows users to search for real-time weather information of any city using the **OpenWeatherMap API**. The app also stores searched weather data in a CSV file and provides options to view and clear past search history.

---

## 🎯 Key Features

* Graphical User Interface using **Tkinter**
* Real-time weather data fetching
* Displays:

  * Weather condition
  * Temperature (°C)
  * Humidity (%)
  * Wind speed (m/s)
* Weather icon display
* Stores search history in a CSV file
* View and clear previous weather searches
* Error handling for invalid city names and empty input

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **Requests** (API calls)
* **Pillow (PIL)** (Image handling)
* **CSV module** (Data storage)
* **OpenWeatherMap API**

---

## 📂 Project Structure

```
Weather-App/
│
├── weather.py              # Main Python application
├── weather_history.csv     # Stores weather search history
├── README.md               # Project documentation
```

---

## ⚙️ Requirements

Ensure you have Python 3 installed. Install the required libraries using:

```
pip install requests pillow
```

---

## 🔑 API Configuration

1. Create an account on **OpenWeatherMap**.
2. Generate your API key.
3. Replace the API key in the code:

```python
api_key = "YOUR_API_KEY"
```

---

## ▶️ How to Run the Application

1. Download or clone the project.
2. Open a terminal in the project directory.
3. Run the Python file:

```
python weather.py
```

4. Enter a city name and click **Get Weather**.

---

## 🧠 How It Works

* The user enters a city name.
* The app sends a request to the OpenWeatherMap API.
* Weather details and icons are displayed on the GUI.
* The data is saved in `weather_history.csv`.
* Users can view or clear previous search history.

---

## 📸 Sample Output

```
Weather: Clear sky
Temperature: 30°C
Humidity: 55%
Wind Speed: 4.2 m/s
```

---

## 📈 Future Enhancements

* Add 5-day weather forecast
* Improve UI design
* Add search by GPS location
* Convert into a desktop executable (.exe)

---


This project is created as a **learning** and **educational purposes**.

---


