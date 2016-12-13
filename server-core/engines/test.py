"""
'test.py' is created by 'invaana' for the project 'chatbot-ai-engine' on 13 December, 2016. 

"""

from scraper import scrape_clean_html


html_data = scrape_clean_html("http://manual.gromacs.org/documentation/2016.1/user-guide/getting-started.html#flowchart-of-typical-simulation")
# print html_data
with open("html_data.txt",'w') as fh:
    fh.write(html_data)