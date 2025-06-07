import streamlit as st

st.set_page_config(page_title="My Streamlit App", layout="centered")

st.title("Welcome to My Streamlit App!")
st.write("This is a simple Streamlit application.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

st.write("Enjoy exploring Streamlit!")