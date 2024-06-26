
import yaml
from yaml.loader import SafeLoader

from src.keeper import Keeper

class Creds():
    def __init__(self) -> None:
        self.config = self.set_config()
        self.username = Keeper().username



    def set_config(self):
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config
    
    def get_nym_key(self):
        key = self.config['credentials']['usernames'][self.username]['api_key']