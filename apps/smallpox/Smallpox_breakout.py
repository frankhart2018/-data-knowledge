import streamlit as st


def app():
    st.markdown("# Smallpox breakout")

    st.markdown("This [dataset](https://www.kaggle.com/datasets/programmerrdai/smallpox-the-presuccessor-to-monkey-pox) contains information about the smallpox breakout in the 17th century which killed approximately 300 million people worldwide, and is considered one of the most deadliest disease ever.")
    st.write("The tasks performed on this can be explored in the pages on the left.")


if __name__ == "__main__":
    app()