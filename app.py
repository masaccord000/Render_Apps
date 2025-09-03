import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="stlite埋め込み", layout="wide")

components.html(
    """
    <iframe src="https://masaccord-static.onrender.com/"
            width="100%" height="700px"
            style="border:none; display:block;"></iframe>
    """,
    height=700
)
