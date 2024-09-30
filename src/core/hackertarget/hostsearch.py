import requests as r
from bs4 import BeautifulSoup
from src.core import user_agent








#https://api.hackertarget.com/hostsearch/?q=

def clean_data(urls: str) -> list:

    urls = urls.replace(',', ' ')
    urls = urls.split()
    links = []
    ips = []
    
    for u in urls:
        if not u[0].isdigit():
            links.append(u)
        else:
            ips.append(u)
    return links

def check_status_code(urls: list) -> list:
    
    urls = clean_data(urls)
    online_urls = []
    for u in urls:
        try:
            response_http = user_agent.req(f'http://{u}/').status_code    
            if response_http != 404:
                online_urls.append(f'http://{u}/')
            else:
                response_https = user_agent.req(f'https://{u}/').status_code
                if response_https != 404:
                    online_urls.append(f'https://{u}/')
        except:
            pass

    return online_urls



def scrap_title(urls: list) -> list:

    #iniciar o scrap_title

    print(urls)

def hostsearch(url: str) -> list:
    api_url = f'https://api.hackertarget.com/hostsearch/?q={url}'
    urls = user_agent.req(api_url).text

    
    for a in check_status_code(urls):
        print(a)




