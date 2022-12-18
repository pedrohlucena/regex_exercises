import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'folder')
) 

with open(os.path.join('.', 'data.txt'), 'r', encoding='utf8') as f:
    data = f.read()
    print(data)
    
    # 1- Statement
    match = re.findall(
        r"""
            # some regex pattern here
        """, 
        data, flags=re.VERBOSE
    )
    print(match)