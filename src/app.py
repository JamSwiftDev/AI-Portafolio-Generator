import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query (payload):
    response = requests.post(HUGGING_FACE_TOKEN, headers=headers, json=payload)
    return response.json()

st.set_page_config(page_title="AI Portfolio Generator", layout="wide")


st.title("🧠 AI Portfolio Generator (Hugging Face API)")

text = st.text_area("Write your project idea:")
if st.button("Generate Summary"):
    if text.strip():
        with st.spinner("Generating..."):
            output = query({"inputs": text})
        st.success(output[0]['summary_text'])