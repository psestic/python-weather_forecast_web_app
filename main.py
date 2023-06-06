import streamlit as st

st.title("Weather Forecast for the Next Days")

# Get input from user
place = st.text_input("Place: ", placeholder="e.g. Amsterdam")
days = st.slider("Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select a number of forecasted days.")
data = st.selectbox("Select data to view",
                    options=('Temperature', 'Sky'))

st.subheader(f"{data} for the next {days} days in {place}")
