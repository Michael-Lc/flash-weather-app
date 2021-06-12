from flask import Flask, render_template, url_for, request, redirect
import requests
import json
from datetime import datetime, date

app = Flask(__name__)


def getWeather(location):
    resp = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key=d2282deb52c74c0691013155210302&q={location}&aqi=no"
    )

    data = json.loads(resp.content)
    location_data = data["location"]
    weather_data = data["current"]
    date_string = datetime.strptime(location_data["localtime"], "%Y-%m-%d %H:%M")
    date = (
        date_string.strftime("%A")
        + ", "
        + str(int(date_string.strftime("%I")))
        + date_string.strftime("%p")
    )

    return {
        "name": location_data["name"],
        "icon": weather_data["condition"]["icon"],
        "text": weather_data["condition"]["text"],
        "temp": str(int(weather_data["temp_c"])),
        "date": date,
    }


@app.route("/", methods=["POST", "GET"])
def index():
    location = "Accra"
    if request.method == "POST":
        query = request.form["search"]
        data = getWeather(query)
    else:
        data = getWeather(location)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)