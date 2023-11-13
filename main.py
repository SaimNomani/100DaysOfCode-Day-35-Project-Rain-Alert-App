# Rain alert app
import requests
from smtplib import SMTP
from data import my_email, my_password, recievers_email, API_KEY
# The provided latitude and longitude values do not indicate my actual position; they are only for testing purposes.
# You can set these according to your location
MY_LATITUDE=-30.60009387355006
MY_LONGITUDE=-56.77734375000001
HOURS=12
parameters={
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "key": API_KEY,
    "hours": HOURS,
}
response=requests.get("https://api.weatherbit.io/v2.0/forecast/hourly", params=parameters)
response.raise_for_status()
weather_data=response.json()['data']
will_rain=False
def send_mail(message:str):
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recievers_email, msg=f"subject:Weather alert\n\n{message}")
for data in weather_data:
    if int(data['weather']['code'])<=700:
        will_rain=True
if will_rain:
    send_mail(message="It's going to rain today. Remember to bring an umbrella.")
else:
    send_mail(message="It's clear today. Have a nice day")
