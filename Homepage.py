
from pprint import pprint
import json

import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

from src.nym_api_inter import nymeria_interface
from src.utils_config import set_config


st.set_page_config(
    page_title="RecruiterCaddy",
    page_icon="wave"
)

config = set_config()


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


    ## Sidebar
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Hello {name}")


    ## File Uploader
    df = st.file_uploader(label='Upload your file')
    if df:
        df = pd.read_csv(df)
        profs = df.loc[:, "Profile URL"]
        profs = profs.to_list()

        contact_res = nymeria_interface(profs, username)
        
        if contact_res:
            for con in contact_res:
                st.divider()
                st.write(f"Full Name: ")
                st.write(f"{con['full_name']}")
                st.write("Phone Numbers: ")
                for numbs in con['ph_nums']:
                    st.write(f"{numbs}")
                st.write("Emails: ")
                for email in con['emails']:
                    st.write(f"{email[1]}")

        else:
            st.write('!!!NONETYPE!!!')




