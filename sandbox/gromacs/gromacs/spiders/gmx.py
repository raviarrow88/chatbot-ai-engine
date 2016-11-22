# -*- coding: utf-8 -*-
import scrapy, sys
from scrapy.selector import Selector


class GromacsSpider(scrapy.Spider):
    name = "gromacs"
    allowed_domains = ["gromacs.org"]
    start_urls = [
        "http://manual.gromacs.org/documentation/2016.1/user-guide/mdp-options.html",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            # STAGE 1: extracting the body html
            body = response.xpath('//body').extract()[0].encode(sys.stdout.encoding, 'replace')
            for el in Selector(text=body).xpath('//*').extract():
                # remove script tag
                if "<script" not in el and "</script>" not in el:

                    # remove styles tag
                    if "<style" not in el and "</style>" not in el:
                        f.write(el.encode(sys.stdout.encoding, 'replace'))
