import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'stocks')
) 

with open(os.path.join('.', 'stocks.txt'), 'r', encoding='utf8') as f:
    stocks_text = f.read()
    print(stocks_text, '\n')
    
    # 1- Match the name of the companies and their revenues if your revenue is less than 50 billion
    less_than_50_billion_companies = re.findall(
        r'(.+?)\s+(?:\d+\.\d+M)\s+([1-4]\d\.\d{2}B)', 
        stocks_text
    )
    print(less_than_50_billion_companies)

    """ 2- Match the name of the companies that have your revenue between 10 billion
    and 30 billion and the P/E ratio between 10 billion and 15 billion."""
    selected_companies = re.findall(
        r'(.+?)\s+(?:\d+\.\d+M)\s+(?:[1-2]\d\.\d+B)\s+(?:1[0-4]\.\d+)', 
        stocks_text
    )
    print(selected_companies)

    """ 3- Match the name of the companies that have your average volume less 
    than 10 million"""
    companies_average_volume_less_than_10M = re.findall(
        r'(.+?)\s+(?:\d\.\d+M).+', 
        stocks_text
    )
    print(companies_average_volume_less_than_10M)

    """ 4- Match the name of the companies that have your average volume starting with
    a even digit and the P/E ratio ending with a odd digit"""
    ood_and_even_companies = re.findall(
        r'(.+?)\s+(?:[2468]\d*\.\d+M)\s+(?:\d+\.\d+B)\s+(?:\d+\.\d+[13579])', 
        stocks_text
    )
    print(ood_and_even_companies)