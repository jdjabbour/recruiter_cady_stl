import pickle
from pathlib import Path

import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

names = ["Peter", "Nancy"]
usernames = ["parker", "drew"]
passwords = ['abc', 'def']

hashed_passwords = Hasher(passwords).generate()

print(hashed_passwords)

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("wb") as file:
#     pickle.dump(hashed_passwords, file)