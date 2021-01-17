# -*- coding: utf-8 -*-
import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for glass in response.xpath("//div[@id = 'product-lists']/div"):

            yield{
                'product name' :glass.xpath(".//div[@class = 'p-title']/a/@title").get(),
                'product price' :glass.xpath(".//div[@class = 'p-price']/div/span/text()").get(),
                'product url' :glass.xpath(".//div[@class = 'product-img-outer']/a/@href").get(),
                'product image link' :glass.xpath(".//img[@class = 'lazy d-block w-100 product-img-default']/@data-src").get()
                
            }


