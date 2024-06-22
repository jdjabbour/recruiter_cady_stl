
import requests


class Call_Api():
    def __init__(self, method, url, headers, payload):
        self.method = method
        self.url = url
        self.headers = headers
        self.payload = payload

    def call_api(self):
        try:
            response = requests.request(
                self.method, 
                self.url, 
                headers=self.headers, 
                data=self.payload
            )
            
            return response
        except Exception as e:
            return e