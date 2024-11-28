import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() ## used to load the environment variables
import os

GOOGLE_API_KEY= "AIzaSyAy-Gd3MMXEEA6_F3pw_BR3uQO7T4sZRHQ"
genai.configure(api_key=GOOGLE_API_KEY)

## function to load the model and get response
model = genai.GenerativeModel("gemini-1.5-pro")
chat=model.start_chat(history=[])

def get_response(question):

    response=chat.send_message(question)
    return response






