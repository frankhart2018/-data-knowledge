import streamlit as st
import streamlit.components.v1 as components


def app():
    st.title("Contents")

    components.html("""
        <ul>
            <li><a href="https://share.streamlit.io/frankhart2018/data-knowledge/apps/smallpox/Smallpox_breakout.py" target="_blank">Smallpox</a></li>
        </ul>
    """)


if __name__ == "__main__":
    app()