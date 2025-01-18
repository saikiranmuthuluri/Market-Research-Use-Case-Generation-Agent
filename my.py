
"""import os
import streamlit as st

# Access the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

print(openai_api_key)"""
import os

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    print("API key is not set.")
else:
    print("API key is:", api_key)