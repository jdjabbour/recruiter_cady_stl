
from pprint import pprint

from src.utils_creds import Creds
from src.nym_call_api import Nymeria_Enrich_Linkedin_Profile
from src.nym_parse import Parse_Contact_Info

def nymeria_interface(profs, username):
    key = Creds().get_nym_key(username)
    api_results = Nymeria_Enrich_Linkedin_Profile(profs, key).enrich_profile()
    api_results = Parse_Contact_Info(api_results).parse_linkedin_contact_info()

    return api_results
