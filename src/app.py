import streamlit as st

st.title("🧠 AI Portfolio Generator")
st.write("Welcome! This app will help you generate and showcase your AI projects easily.")

name = st.text_input("Enter your name")
bio = st.text_area("Write a short bio about yourself")

if st.button("Generate Portfolio"):
    if name and bio:
        st.success(f"Portfolio generated for {name}!")
        st.write(f"**Bio:** {bio}")
    else:
        st.warning("Please fill in both your name and bio.") 