import streamlit as st


st.title("Contact")

my_input = st.session_state["my_input"]
st.write("You have entered: ", my_input)