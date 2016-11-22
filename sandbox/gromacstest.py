# -*- coding: utf-8 -*-
import scrapy


class GromacsSpider(scrapy.Spider):
    name = "gromacs"
    allowed_domains = ["gromacs.org"]
    start_urls = [
        "http://manual.gromacs.org/documentation/2016.1/user-guide/mdp-options.html",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)