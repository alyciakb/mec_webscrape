# -*- coding: utf-8 -*-
import scrapy


class MecspiderSpider(scrapy.Spider):
    name = 'mecspider'
    allowed_domains = ['mec.ca']
    start_urls = ['https://www.mec.ca/en/products/c/100']

    def parse(self, response):
        # get the text name of the product
        title = response.css(".product__name__link.qa-product__name__link.js-grid-url.js-product-click-track-link.js-product-view-track::text").extract()
        products = response.css("a.rating__count__link::attr(title)").extract()


        for item in zip(title, products):
            #create a dictionary to store the scraped info
            product_info = {
                'title' : item[0],
                'product' : item[1]
                }
            yield product_info

        # scrape next page if there is a next page
        next_page_exists = response.css("li.pagination__item > a::attr(rel)").extract()
        for value in next_page_exists:
            if value == "next":
                url_add = response.css("li.pagination__item > a.pagination__link.pagination__link--next.qa-pagination__link--next.js-product-tile-takeover__next-page::attr(href)").extract_first()
                yield response.follow(url_add, callback=self.parse)



        # link to product page (to extract reviews)
        #product_links = response.css(".rating__count__link.js-product-click-track-link::attr(href)").extract()
        #for link in product_links:
            # need to put full url here
            # baseurl + link
            #product = response.css(".product__name.t-level-3.qa-product__name.u-block::text").extract_first()
            #product_code =  response.css(".product__code.text--subtle::text").extract_first()
