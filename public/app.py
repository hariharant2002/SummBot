import streamlit as st

# Read the HTML file
with open('public\index.html', 'r') as file:
    html_content = file.read()

# Display the HTML file in Streamlit
st.components.v1.html(html_content, height=600)
