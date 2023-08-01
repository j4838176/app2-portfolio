import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I am Ardit! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013.
    I have worked with companies from various countries, such as the Center for Conservation Geography.
    """
    st.info(content)
