
from src.utils_creds import Creds
from src.utils_nym_api import Nymeria_Enrich_Linkedin_Profile

def nymeria_interface(profs):
    key = Creds().get_nym_key()
    contact_results = Nymeria_Enrich_Linkedin_Profile(profs, key).enrich_profile()
