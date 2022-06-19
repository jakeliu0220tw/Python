import os
from setting import *

def get_setting():
    env = os.getenv('ENV', 'prod')
    if env == 'prod':
        return ProdSetting()
    else:
        return TestSetting()

s = get_setting()
print(f"type(s) = {type(s)}")
print(f"s = {s.dict()}")
print(f"API_BASE = {os.getenv('API_BASE', '')}")
print(f"s.API_BASE = {s.API_BASE}")
