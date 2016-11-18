# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["i-hong.com"]
    start_urls = ['http://i-hong.com/']

    def parse(self, response):
        pass
