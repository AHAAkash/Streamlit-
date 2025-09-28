import streamlit as st
import os

st.title("Hello, Streamlit!")
st.write("This is a simple Leaning app using Streamlit.")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a markdown text")
st.caption("Small text")
code_example = """
def hello():
    print("Hello, Streamlit!")
"""
st.code(code_example, language="python")
st.json({"name": "Streamlit", "type": "Library", "language": "Python"})
st.latex(r"E=mc^2")
st.metric("Temperature", "25 °C", "+1.5 °C")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "download.png"))  #Os.path.join is used to make it work in any OS and join something to the current working directory (getcwd = get current working directory)
