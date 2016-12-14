# -*- coding: utf-8 -*-
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

    """
    This method takes url as inputs and outputs the plane html without dirty classes,
    <script>, <style> tags

    :param url: a valid url,
    :return:
    """

    clean_html =  lxml.html.tostring(cleaner.clean_html(lxml.html.parse(url)))
    doc = fromstring(clean_html)
    TO_CLEAN_TAGS = ['div','li','ul','h1','h2','h3','h4','h5','h6','p','a','img','span','code', 'pre',
                     'ol','li', 'dl', 'section','nav']

    TO_REMOVE_ATTR = ['class','title','rel','alt','height','width','id','accesskey']

    """
    id is an important attribute, sometimes it links the two things, but pointing as
    link
    """

    # TO_EXCEPT_IDS = ['a', 'div']
    TO_REMOVE_BLANK_TAGS = ['div','section','span','a']

    for tag in TO_CLEAN_TAGS:
        for el in doc.iter(tag):
            # if tag not in TO_EXCEPT_IDS:
            #     if "id" in el.attrib:
            #         del el.attrib['id']

            if 'href' in el.attrib:
                if el.attrib['href'].startswith('#'):
                    del el.attrib['href']

            for ex in TO_REMOVE_ATTR:
                if ex in el.attrib:
                    del el.attrib[ex]




    final_cleaned_html =  _transform_result(type(clean_html), doc)
    """
    soup = BeautifulSoup(final_cleaned_html, 'lxml')
    final_cleaned_body = soup.body.encode('utf-8')

    with open("final_cleaned_html.txt",'w') as f:
        f.write(final_cleaned_html)
    """
    final_cleaned_html.replace('¶','')

    soup = BeautifulSoup(final_cleaned_html,'lxml')
    final_cleaned_html = soup.body.encode("utf-8")
    elements = soup.find_all(True)

    #with open("html_data1.log", 'w') as file1:
    for el in elements:
        if len(el.text) == 0:
            el.extract()
    print soup
    '''
            if el.encode("utf-8").lower().lstrip().startswith("<h"):
                text = el.get_text()
                el.string = text
                print el.string
            file1.write(str(el))
    '''
    for tag in TO_REMOVE_BLANK_TAGS:
        final_cleaned_html = final_cleaned_html.replace("<%s>"%tag,'').replace('</%s>'%tag,'')



    return BeautifulSoup(final_cleaned_html,'lxml').body.prettify().encode('utf-8')


