import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path

import yaml
from yaml.loader import SafeLoader

import streamlit_authenticator as stauth


st.set_page_config(
    page_title="Multi-App",
    page_icon="wave"
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# names = ["Peter"]
# usernames = {"Peter": "parker"}

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login()

if authentication_status == False:
    st.error("Username/Password are not Correct")

if authentication_status == None:
    st.warning("Please enter your credentials")

if authentication_status:

    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Hello {name}")
    st.sidebar.success("Select a page above")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")

    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered: ", my_input)


# with st.sidebar:
#     selected = option_menu(
#         # Required
#         menu_title="Main Menu",
#         # Required
#         options=["Home", "Projects", "Contact"],

#         # Optional

#         # Get icons from the bootstrap site.  
#         # You just need the name of the icon
#         icons = ["house", "book", "envelope"], 
#         menu_icon="cast",
#         default_index=0

#     )


# if selected == "Home":
#     st.title(f"You have selected: {selected}")
# if selected == "Projects":
#     st.title(f"You have selected: {selected}")
# if selected == "Contact":
#     st.title(f"You have selected: {selected}")