"""
'scraper.py' is created by 'invaana' for the project 'chatbot-ai-engine' on 13 December, 2016. 

"""

"""
'test.py' is created by 'invaana' for the project 'chatbot-ai-engine' on 13 December, 2016.


References :
http://stackoverflow.com/questions/7470333/remove-certain-attributes-from-html-tags
"""

from bs4 import BeautifulSoup
import lxml.html
import lxml
from lxml.html.clean import Cleaner
from lxml.html import fromstring
from lxml.html import _transform_result

cleaner = Cleaner()
cleaner.javascript = True # This is True because we want to activate the javascript filter
cleaner.style = True      # This is True because we want to activate the styles & stylesheet filter



def scrape_clean_html(url):
    clean_html =  lxml.html.tostring(cleaner.clean_html(lxml.html.parse(url)))
    doc = fromstring(clean_html)



    tags = ['div','li','ul','h1','h2','h3','h4','h5','h6','p','a','img']


    for tag in tags:
        for el in doc.iter(tag):
            if "class" in el.attrib:
                del el.attrib["class"]


    final_cleaned_html =  _transform_result(type(clean_html), doc)
    """
    soup = BeautifulSoup(final_cleaned_html, 'lxml')
    final_cleaned_body = soup.body.encode('utf-8')

    with open("final_cleaned_html.txt",'w') as f:
        f.write(final_cleaned_html)
    """

    return final_cleaned_html


