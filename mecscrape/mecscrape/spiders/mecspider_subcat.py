# -*- coding: utf-8 -*-
import scrapy

class Mecspider2Spider(scrapy.Spider):
    name = 'mecspider2'
    allowed_domains = ['mec.ca']
    start_urls = ['https://www.mec.ca/en/products/c/100']

    def parse(self, response):

        # get the product categories
        #prod_categories = response.css("h3.subcategory-nav__header.subcategory-nav__header-link.js-promo-click-track-link::text").extract()
        # get links to product categories
        #prod_categories_links = response.css("div.subcategory-nav.subcategory-nav--bordered.js-promo > a.subcategory-nav__image.js-promo-click-track-link::attr(href)").getall()
        prod_categories_links = response.css("li.list__item.qa-facet-list__item > a::attr(href)")[:-1].getall()

        for link in prod_categories_links:
            yield response.follow(link, callback=self.subcategory)

    def subcategory(self, response):
        #subcategories_links = response.css("ul.list.list--tree.list--active.list--limit.js-facet-list > li.list__item.qa-facet-list__item > a::attr(href)").getall()
        subcategories_links = response.css("li.list__item.qa-facet-list__item > a::attr(href)")[2:].getall()
        for sublink in subcategories_links:
            yield response.follow(sublink, callback=self.parse_items)

    def parse_items(self, response):
        prod_category = response.css("li.breadcrumbs__item > a.breadcrumbs__text::text")[-1].get()
        prod_subcategory = response.css("span.breadcrumbs__text::text").get()

        # get the text name of the product
        title = response.css(".product__name__link.qa-product__name__link.js-grid-url.js-product-click-track-link.js-product-view-track::text").getall()
        products = response.css("a.rating__count__link::attr(title)").getall()


        for item in zip(title, products):
            #create a dictionary to store the scraped info
            product_info = {
                'category' : prod_category,
                'subcategory' : prod_subcategory,
                'title' : item[0],
                'product' : item[1]
                }
            yield product_info

        # scrape next page if there is a next page
        next_page_exists = response.css("li.pagination__item > a::attr(rel)").getall()
        if not next_page_exists:
            pass
        else:
            for value in next_page_exists:
                if value == "next":
                    url_add = response.css("li.pagination__item > a.pagination__link.pagination__link--next.qa-pagination__link--next.js-product-tile-takeover__next-page::attr(href)").get()
                    yield response.follow(url_add, callback=self.parse_items)
