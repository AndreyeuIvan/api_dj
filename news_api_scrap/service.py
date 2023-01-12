import os
import requests
from dotenv import load_dotenv

load_dotenv()


Key = os.environ.get('API')

def get_news(query:str):
    api= f"https://newsapi.org/v2/everything?q={query}&apiKey={Key}"
    req = requests.get(api)
    #import pdb;pdb.set_trace()
    return req.json()
