import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.chdir(
    os.path.join(os.getenv('REPO_PATH'), 'bookshelf')
) 

with open(os.path.join('.', 'bookshelf.txt'), 'r', encoding='utf8') as f:
    bookshelf_text = f.read()
    print(bookshelf_text)
    
    # 1- Match all the books that have your name longer than 25 characters
    book_names_longer_than_25_characters = re.findall(
        r"""
            .+?; # author name
            (.{1,25}); # book name longer than 25 characters
            .+? # book release year
        """, 
        bookshelf_text, flags=re.VERBOSE
    )
    print(book_names_longer_than_25_characters)

    # 2- Match all the authors that released your books after 2000
    authors_after_2000 = re.findall(
        r"""
            (.+?); # author name
            .+?; # book name
            2\d{3,} # book release year after 2000
        """, 
        bookshelf_text, flags=re.VERBOSE
    )
    print(authors_after_2000)

    # 3- Match all the book titles that end with the letter p
    book_titles_ending_with_p = re.findall(
        r"""
            .+?; # author name
            (.+p); # book name ending with the "p" letter
            .+? # book release year
        """, 
        bookshelf_text, flags=re.VERBOSE
    )
    print(book_titles_ending_with_p)

    # 4- Match all the author last names that starts with "B"
    authors_with_last_name_B = re.findall(
        r"""
            .+\b(B.+?); # author last name that starts with "B"
            .+?; # book name
            .+? # book release year
        """, 
        bookshelf_text, flags=re.VERBOSE
    )
    print(authors_with_last_name_B)

    # 5- Match all the book names that have been released between 1980 and 1999
    book_released_between_1980_and_1999 = re.findall(
        r"""
            .+?; # author name
            (.+?); # book name
            19[89][0-9] # 1980-1999 date range
        """, 
        bookshelf_text, flags=re.VERBOSE
    )
    print(book_released_between_1980_and_1999)