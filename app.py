import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="統合ビュー", page_icon="🧩", layout="wide")

st.title("🧩 stlite アプリの埋め込み表示")
st.write("以下は Render Static Site で公開された stlite アプリです：")

components.html(
    """
    <iframe src="https://masaccord-static.onrender.com/" width="100%" height="800px" style="border:none;"></iframe>
    """,
    height=800
)
