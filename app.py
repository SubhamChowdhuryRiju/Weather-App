import requests
import streamlit as st 
import json 

st.title("Weather Application")

with open('data.json', 'r') as file:
    data = json.load(file)

states = data.keys()

city_name = ""

st.subheader("Select the State")
state_name = st.selectbox(label="Select the State", options=states)

if state_name:
    cities = data[state_name]
    st.subheader("Select the City")
    city_name = st.selectbox(label="Select the City", options=cities)


if city_name:
    api_key = "f09c8818b978dbb75c0a83da4c21767b"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_name}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.write(f"Current Weather Condition: {data['weather'][0]['main']}.")
        st.write(f"Current Tempurature: {data['main']['temp']}°C.")
        st.write(f"Tempurature Feels Like: {data['main']['feels_like']}°C.")
        st.write(f"Humidity: {data['main']['humidity']}%.")
    else:
        st.error("Error Occured, Please check the City Name or the State Name is correct or not!")