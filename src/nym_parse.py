



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