
from pprint import pprint

from src.utils_call_api import Call_Api


class Nymeria_Enrich_Linkedin_Profile():
    """
    This class is used to enrich a candidate's info
    using a profile from linkedin
    """
    def __init__(self, profs, api_key):
        self.profiles = profs  # List
        self.api_key = api_key
        self.headers = None
        self.payload = []
        self.base_url = "https://www.nymeria.io/api/v4/person/enrich"
        self.method_get = 'GET'


    def enrich_profile(self):
        """
        Driver Merthod
        """
        for prof in self.profiles:
            prof = self.clean_profile(prof)
            prof = self.add_profile_query(prof)
            url = self.build_url(prof)
            self.headers = self.build_headers()
            api_res = self.call_nym_api(url)
            st_code = self.get_status_code(api_res)
            if st_code == 200 or st_code == '200':
                api_res = self.jsonify_results(api_res)
                self.payload.append(api_res)


        return self.payload
            

    def clean_profile(self, prof):
        prof = prof.strip()
        prof = prof.replace('https://www.', '')
        return prof

    def add_profile_query(self, prof):
        prof = f'?profile={prof}'
        return prof
    
    def build_url(self, prof):
        url = f"{self.base_url}{prof}"
        return url

    def build_headers(self):
        header = {
            'X-Api-Key': f"{self.api_key}"
        }
        return header
    
    def call_nym_api(self, url):
        try:
            payload = {}
            api_res = Call_Api(self.method_get, url, self.headers, payload).call_api()
            return api_res
        except Exception as e:
            print(f"CALL NYMERIA API ERROR: {e}")

    def get_status_code(self, api_res):
        try:
            st_code = api_res.status_code
            return st_code
        except Exception as e:
            print(f"ERROR: {e}")

    def jsonify_results(self, api_res):
        api_res = api_res.json()
        api_res = api_res['data']
        return api_res

