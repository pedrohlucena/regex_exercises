import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'logs')
) 

with open(os.path.join('.', 'logs.txt'), 'r', encoding='utf8') as f:
    logs_text = f.read()
    print(logs_text)
    
    # 1- Get all the critical logs that were generated between 2020-01-11 and 2020-01-16
    critical_logs_in_a_period = re.findall(
        r'Critical 1\/1[1-6]\/2020 .+ [A-Z]{2} (.+?) \d+', 
        logs_text
    )
    print(critical_logs_in_a_period)

    # 2- Get the source of the logs generated after 12PM and before 4PM
    logs_after_12AM_and_before_4PM = re.findall(
        r'.+? \d{1,2}\/\d{2}\/\d{4} (?:(?:12|[1-3]):\d{2}:\d{2}) PM (.+?) .+', 
        logs_text
    )
    print(logs_after_12AM_and_before_4PM)

    # 3- Get the date of the logs that has "TPM" as source
    TPM_date_logs = re.findall(
        r'.+? (.+?) \d+:\d+:\d+ (?:AM|PM) TPM', 
        logs_text
    )
    print(TPM_date_logs)

    """ 4- Get the date and time of the logs that has generated between 24 and 27 of
    January 2020 and between 8:00:00 and 8:59:59 AM"""
    logs_in_specific_period = re.findall(
        r'.+? (1\/2[4-7]\/2020 8:[0-5][0-9]:[0-5][0-9])', 
        logs_text
    )
    print(logs_in_specific_period)