import streamlit as st
import plotly.express as px
from get_data import get_data

st.title("Weather Forecast for the next Days")

# Get input from user
place = st.text_input("Place: ",
                      placeholder="Enter a city name (e.g. Amsterdam)")
if not place:
    place = "Amsterdam"
days = st.slider("Forecast Days",
                 min_value=1,
                 max_value=5,
                 value=2,
                 help="Select a number of forecasted days.",
                 )
datatype = st.selectbox("Select data to view",
                        options=('Temperature', 'Sky'))

try:
    st.subheader(f"{datatype} for the next {days} days in {place.title()}")

    # Get data from API
    filtered_data = get_data(place, days)

    if datatype =="Temperature":
        temperatures = [(dictionary["main"]["temp"]/10) for dictionary in filtered_data]
        dates = [dictionary["dt_txt"] for dictionary in filtered_data]
        # Plot temperature graph
        figure = px.line(x=dates,
                         y=temperatures,
                         labels={"x": "Dates", "y": "Temperatures (C)"})
        st.plotly_chart(figure)

    if datatype == "Sky":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dictionary["weather"][0]["main"] for dictionary in filtered_data]
        dates = [dictionary["dt_txt"] for dictionary in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, caption=dates, width=115)
except KeyError:
    st.info("Please enter a valid name of a place!")