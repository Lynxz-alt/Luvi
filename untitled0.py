import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Streamlist Luvi", layout="wide")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

with open("streamlist-luvi.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=900, scrolling=True)

