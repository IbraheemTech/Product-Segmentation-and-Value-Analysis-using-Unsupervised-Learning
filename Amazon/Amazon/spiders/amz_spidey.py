import scrapy
from .. items import AmazonItem


class AmzSpideySpider(scrapy.Spider):
    name = "amz_spidey"
    start_urls = [
        "https://www.amazon.com/s?k=kitchen+and+dining&i=kitchen-intl-ship"]
    base_url = "https://www.amazon.com/s?k=kitchen+and+dining&i=kitchen-intl-ship"
    page_limit = 70


#    def start_request(self):
#        keyword_list1 = ['kitchen+and+dining']
#        keyword_list2 = ['kitchen-intl-ship']
#        for keyword in keyword_list1 & keyword_list2:
#            amz_search_url = f'https://www.amazon.com/s?k={keyword_list1}&i={keyword_list2}&page=1'
#            yield scrapy.Request(url=amz_search_url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': 1})

    def parse(self, response):

        data = response.css('.a-section.a-spacing-base')

        for product in data:
            items = AmazonItem()
            items['product_name'] = product.css(
                'span.a-size-base-plus.a-color-base.a-text-normal::text').extract()
            currency_symbol = product.css('span.a-price-symbol::text').get()
            whole_price = product.css('span.a-price-whole::text').get()
            decimal_price = product.css('span.a-price-decimal::text').get()
            fractional_price = product.css('span.a-price-fraction::text').get()
            if currency_symbol is not None and whole_price is not None and decimal_price is not None and fractional_price is not None:
                price_parts = currency_symbol + whole_price + decimal_price + fractional_price
            else:
                price_parts = None  # Handle the case where any part is missing
            # price_parts = product.css('span.a-price-symbol::text').get() + product.css('span.a-price-whole::text').get() + product.css('span.a-price-decimal::text').get() + product.css('span.a-price-fraction::text').get()

            items['product_price'] = f"{price_parts}"
            rating = product.css(
                'span.a-size-base.puis-bold-weight-text::text').extract()
            if rating:
                items['product_rating'] = rating
            else:
                items['product_rating'] = "No Rating"
            items['product_image'] = product.css(
                '.s-image::attr(src)').extract()

            yield items

        # Pagination Logic
        page_number = response.meta.get('page', 1)
        if page_number <= self.page_limit:
            next_page_url = f"{self.base_url}&page={page_number + 1}"
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'page': page_number + 1})
