import pyshorteners 
import streamlit as st

def shorten_url(url):
    # Shortening the url
    s = pyshorteners.Shortener()
    shorten_url = s.tinyurl.short(url)
    return shorten_url

#creamos  la interfaz de usuario
st.set_page_config(page_title="URL Shortener", page_icon="🔗")
st.title("URL Shortener")
url= st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("Shortened URL:", shorten_url(url))
    