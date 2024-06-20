
import requests

from pprint import pprint
import psycopg2





class Nymeria_Api():
    """
    This gets inherited by the other Nymeria classes
    """
    def __init__(self):
        self.base_url = "https://www.nymeria.io/api/v4/person/enrich"
        self.method_post = 'POST'
        self.method_get = 'GET'



class Enrich_Linkedin_Profile(Nymeria_Api):
    """
    This class is used to enrich a candidate's info
    using a profile from linkedin
    """
    def __init__(self, profs, api_key):
        super().__init__()
        self.profiles = profs
        self.api_key = api_key
        self.headers = None
        self.payload = []


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
            if st_code == 200:
                api_res = self.jsonify_results(api_res)
                self.payload.append(api_res)
            else:
                print(f"NO: {url}")

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
            api_res = Call_Api(self.method_get, url, self.headers, self.payload).call_api()
            return api_res
        except Exception as e:
            print(f"NYMERIA API ERROR: {e}")

    def get_status_code(self, api_res):
        try:
            st_code = api_res.status_code
            return st_code
        except Exception as e:
            print(f"")

    def jsonify_results(self, api_res):
        api_res = api_res.json()
        api_res = api_res['data']
        return api_res



class Parse_Contact_Info():
    def __init__(self, payload):
        self.payload = payload
        self.results = {}
        self.profiles = []

    def parse_linkedin_contact_info(self):
        for prof in self.payload:
            self.get_full_name(prof)
            self.get_emails(prof)
            self.get_mobile_phone_number(prof)
            self.get_phone_numbers(prof)
            self.scrub_phone_numbers()
            self.profiles.append(self.results)

        return self.profiles
        
    def get_full_name(self, prof):
        self.results['full_name'] = prof['full_name']
        return self.results

    def get_emails(self, prof):
        self.results['emails'] = []
        email_srch = prof['emails']
        for email in email_srch:
            addy_type = email['type']
            email_addy = email['address']
            email = (addy_type, email_addy)
            self.results['emails'].append(email)
        return self.results
    
    def get_mobile_phone_number(self, prof):
        self.results['mobile_ph'] = prof['mobile_phone']
        return self.results

    def get_phone_numbers(self, prof):
        self.results['ph_nums'] = prof['phone_numbers']
        return self.results
    
    def scrub_phone_numbers(self):
        phone_numbs = []
        ph_numbs = self.results['ph_nums']
        for ph_numb in ph_numbs:
            if len(ph_numb) == 11:
                ph_numb = f"{ph_numb[0]}-{ph_numb[1:4]}-{ph_numb[4:7]}-{ph_numb[7:]}"
                phone_numbs.append(ph_numb)
            elif len(ph_numb) == 10:
                ph_numb = f"{ph_numb[0:3]}-{ph_numb[3:6]}-{ph_numb[6:]}"
                phone_numbs.append(ph_numb)
            else:
                phone_numbs.append(ph_numb)
        self.results['ph_nums'] = phone_numbs
        return self.results



class Call_Api():
    def __init__(self, method, url, headers, payload):
        self.method = method
        self.url = url
        self.headers = headers
        self.payload = payload

    def call_api(self):
        try:
            response = requests.request(self.method, self.url, headers=self.headers, data=self.payload)
            return response
        except Exception as e:
            return e



def upload_results_to_db(profiles):
    for prof in profiles:
        print(prof)
        try:
            row = app_tables.linkedinresults.add_row(name=prof['full_name'] ,emails=str(prof['emails']), phone_numbers=str(prof['ph_nums']))
            return 1
        except Exception as e:
            print(f"ERROR: {e}")
            return 0


@anvil.server.callable
def frontend_db_query():
    rows = app_tables.linkedinresults.search()
    return rows
    # conn = psycopg2.connect(anvil.tables.get_connection_string())
    # with conn.cursor() as cur:
    #     cur.execute("SELECT * FROM LinkedinResults")
    #     results = list(cur)
    #     for r in results:
    #         print(r)
    #     return results