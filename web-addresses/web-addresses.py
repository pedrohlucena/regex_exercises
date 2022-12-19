import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'web-addresses')
) 

with open(os.path.join('.', 'web.txt'), 'r', encoding='utf8') as f:
    web_text = f.read()
    print(web_text,'\n')
    
    # 1- Get all the URLs of the sites that provides online shopping services
    online_shopping_sites_urls = re.findall(
        r'.+\s+(https?.+\.\w{2,})\t\d+ .+Online shopping.+', 
        web_text,
    )
    print(online_shopping_sites_urls)

    """2- Get the name of the sites that have a 3 letter URL extension (.org, .com, .net)
    and are based on China"""
    online_shopping_sites_urls = re.findall(
        r'(.+)\s+(?:https?.+\.\w{3})\s.+China.+', 
        web_text,
    )
    print(online_shopping_sites_urls)

    """3- Match the URL and the country of the sites that provide Social Networking
    services and has your domain name with less than 5 characters"""
    social_networking_sites_less_than_5_characters = re.findall(
        r'(?:.+)\s+(https?:\/\/.{1,4}\.\w{2,})\s.+Social networking\s(.+?)\s.+', 
        web_text,
    )
    print(social_networking_sites_less_than_5_characters)

    """4- Get the name and the protocol of all the sites that have subdomains
    (e.g. http://something.website.abc)"""
    sites_with_subdomains = re.findall(
        r'(.+)\s+(?:(https?):\/\/.+\..+\.\w{2,}).+', 
        web_text,
    )
    print(sites_with_subdomains)