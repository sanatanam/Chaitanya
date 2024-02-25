#AIzaSyAo4Vdfe3-FQT2AzyqKbPXJ-R2c2JaupJk

# Install the package if needed (uncomment this line if you haven't installed it yet)
# pip install google-generativeai

import google.generativeai as genai
from prompt_toolkit import prompt, print_formatted_text, HTML
import pyttsx3
import speech_recognition as sr
import streamlit as st

r = sr.Recognizer()

engine = pyttsx3.init()

# Set voice rate (optional)
engine.setProperty('rate', 150)


# Configure API key (replace with your actual API key)
genai.configure(api_key="AIzaSyAo4Vdfe3-FQT2AzyqKbPXJ-R2c2JaupJk")

# Set up generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Set up safety filters
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)
# Define colors
USER_COLOR = "blue"
OUTPUT_COLOR = "orange"

# Header
# Header
st.markdown(
    """
    <h1 style="background-color: black; color: white; text-align: center; padding: 20px;">
        <span style="font-weight: bold;">Chaitanya</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.markdown(
    """
    <p style="text-align: center;">
        Namaste️ Welcome to the future of conversations! I'm Chaitanya, your friendly AI assistant, the brainchild of Sanatanam, crafted with passion by Pranav Visen. Let's dive into a world of endless possibilities together. Ask me anything or simply drop a 'hello' – the pleasure is all mine! ✨
    </p>
    """,
    unsafe_allow_html=True
)

# User input and response (placed at the bottom)
st.markdown("")  # Add some space before the input section

user_input = st.text_input("You:", key="user_input")
send_button = st.button("Send", type="primary", key="send_button")

# Generate response
response = model.generate_content([user_input])

# Display response
st.markdown(f"**You:** {user_input}", unsafe_allow_html=True)
st.markdown(f"**Chaitanya:** {response.text}", unsafe_allow_html=True)
