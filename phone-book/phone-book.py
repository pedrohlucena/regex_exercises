import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'phone-book')
) 

with open(os.path.join('.', 'phone.txt'), 'r', encoding='utf8') as f:
    phone_text = f.read()
    print(phone_text)
    
    """1- Match the last name and the phone number of the people that have the area 
    number of their phones terminating with 0"""
    names_and_phones = re.findall(
        r'(?:.+) (.+)\s+(?:\(\d{2}0\))\s+(\d{3}-\d{4})', 
        phone_text
    )
    print(names_and_phones)    

    #2- Match the area codes of the phone numbers ending with 7
    area_codes_numbers_ending_with_7 = re.findall(
        r"""
            (?:.+) # first name
            \s+ # set of whitespace characters
            (?:.+) # last name
            \s+
            \(
            (\d{3}) # area code
            \)
            \s+
            (?:\d{3}-\d{3}7) # phone number ending with 7
        """, 
        phone_text, flags=re.VERBOSE
    )
    print(area_codes_numbers_ending_with_7)   

    #3- Match persons with the phone number starting with an odd digit
    persons_with_number_start_odd_digit = re.findall(
        r"""
            (.+) # person name
            \t
            (?:\(\d{3}\)) # area code
            \s+ # set of whitespace characters
            (?:[13579]\d{2}-\d{4}) # phone number starting with an odd digit
        """, 
        phone_text
    )
    print(persons_with_number_start_odd_digit)

    #4- Match all the persons first names that has the area code of their phone numbers less than 300
    persons_with_number_start_odd_digit = re.findall(
        r'(.+) +(?:.+)\s+(?:\([0-2]\d\d\))\s+(?:\d{3}-\d{4})', 
        phone_text
    )
    print(persons_with_number_start_odd_digit)

    """5- Match all the persons first names that your last name ending with a vowel and your 
    phone number ends with the digits "0" "7" or "9" """
    selected_persons = re.findall(
        r'(.+) +(?:.+[aeiou])\s+(?:\(\d{3}\))\s+(?:\d{3}-\d{3}[079])', 
        phone_text
    )
    print(selected_persons)