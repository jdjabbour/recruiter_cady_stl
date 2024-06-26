
from utils_creds import Creds
from nym_call_api import Nymeria_Enrich_Linkedin_Profile

def nymeria_interface(profs, username):
    key = Creds().get_nym_key(username)
    contact_results = Nymeria_Enrich_Linkedin_Profile(profs, key).enrich_profile()
