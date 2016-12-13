"""
'test.py' is created by 'invaana' for the project 'chatbot-ai-engine' on 13 December, 2016. 

"""

from scraper import scrape_clean_html


html_data = scrape_clean_html("http://stackoverflow.com/questions/7470333/remove-certain-attributes-from-html-tags")
print html_data