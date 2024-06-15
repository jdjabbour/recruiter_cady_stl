
import yaml
from yaml.loader import SafeLoader

def set_config():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config