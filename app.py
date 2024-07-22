import streamlit as st
import requests
import json
import base64

OPENWEATHER_API_KEY = '033f19189a8ab629d8ac47ab098e86ef'

# Function to convert image file to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        img_bytes = image_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()
    return img_base64

# Path to your local background image
image_path = 'background_light.jpg'  # Update this path to your image

# Convert the image to base64
img_base64 = image_to_base64(image_path)

# Streamlit app configuration
st.set_page_config(page_title='Weather App', page_icon=':sunny:', layout='wide')

# Custom CSS for background image and styling
st.markdown(f"""
    <style>
    body {{
        background-color: #f0f0f0;
    }}
    .main {{
        background-image: url(data:image/jpeg;base64,{img_base64});
        background-size: cover;
        background-position: center;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }}
    .header {{
        text-align: center;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 3em;
        font-weight: bold;
        padding: 20px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .sidebar {{
        background-color: rgba(0, 0, 0, 0.7);
        color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    }}
    .footer {{
        text-align: center;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        color: #ffffff;
        border-radius: 10px;
        font-family: 'Roboto', sans-serif;
    }}
    .stTextInput input {{
        border-radius: 5px;
        padding: 10px;
        border: 2px solid #ffffff;
        background-color: rgba(0, 0, 0, 0.3);
        color: #ffffff;
    }}
    .stButton {{
        background-color: #007bff;
        color: #ffffff;
        border-radius: 5px;
        padding: 10px;
        border: none;
        cursor: pointer;
    }}
    .stButton:hover {{
        background-color: #0056b3;
    }}
    .stSuccess {{
        background-color: rgba(0, 255, 0, 0.2);
        color: #ffffff;
        border: 2px solid #00ff00;
        border-radius: 5px;
        padding: 10px;
    }}
    .stError {{
        background-color: rgba(255, 0, 0, 0.2);
        color: #ffffff;
        border: 2px solid #ff0000;
        border-radius: 5px;
        padding: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>Weather App</div>", unsafe_allow_html=True)

# Sidebar for additional user interaction
with st.sidebar:
    st.markdown("<h2>Weather Information</h2>", unsafe_allow_html=True)
    st.write("This app provides the current temperature of any city you enter.")
    st.write("**Instructions**:")
    st.write("- Enter the city name in the text box.")
    st.write("- Click the search button or press Enter.")
    st.write("- View the temperature in Celsius.")

# Main content
st.markdown("<div class='main'>", unsafe_allow_html=True)
city_name = st.text_input("Enter city name:", placeholder="E.g., Palakollu")

if city_name:
    with st.spinner('Fetching data...'):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}')
        data = json.loads(response.text)

        if data['cod'] == 200:
            temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            st.success(f'The current temperature in {city_name} is {temp:.2f}°C.')
        else:
            st.error('Sorry, I could not find that city. Please check the city name and try again.')

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed with ❤️ by [U.N.V.RAVI TEJA]</div>", unsafe_allow_html=True)
