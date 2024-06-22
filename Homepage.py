import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


import src

import streamlit_authenticator as stauth

import src.utils_config


st.set_page_config(
    page_title="Multi-App",
    page_icon="wave"
)

config = src.utils_config.set_config()


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login()

api_key = config['credentials']['usernames'][username]['api_key']


if authentication_status == False:
    st.error("Username/Password are not Correct")


if authentication_status == None:
    st.warning("Please enter your credentials")


if authentication_status:

    ## Sidebar
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Hello {name}")
    # st.sidebar.success("Select a page above")

    ## User input
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")

    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered: ", my_input)

    ## File Uploader
    df = st.file_uploader(label='Upload your file')
    if df:
        df = pd.read_csv(df)
        profs = df.loc[:, "Profile URL"]
        profs = profs.to_list()


        print(f"PROFS: {profs}")

