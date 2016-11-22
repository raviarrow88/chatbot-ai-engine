# -*- coding: utf-8 -*-
import scrapy, sys


class GromacsSpider(scrapy.Spider):
    name = "gromacs"
    allowed_domains = ["gromacs.org"]
    start_urls = [
        "http://manual.gromacs.org/documentation/2016.1/user-guide/mdp-options.html",
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)


        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            d = response.xpath('//body').extract()[0].encode(sys.stdout.encoding, 'replace')
            print d
            f.write(d)
        #
        #
        # for sel in response.xpath('//ul/li'):
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print title, link, desc