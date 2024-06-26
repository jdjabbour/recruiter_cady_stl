import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit_authenticator as stauth

from src.keeper import Keeper

from src.inter_nym_api import nymeria_interface
from src.utils_config import set_config


st.set_page_config(
    page_title="Multi-App",
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

    Keeper(username, name, authentication_status)

    ## Sidebar
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Hello {name}")


    ## File Uploader
    df = st.file_uploader(label='Upload your file')
    if df:
        df = pd.read_csv(df)
        profs = df.loc[:, "Profile URL"]
        profs = profs.to_list()

        contact_res = nymeria_interface(profs)



