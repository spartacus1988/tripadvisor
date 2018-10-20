import re
import time

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from tripadvisor.items import *
from tripadvisor.spiders.crawlerhelper import *


# Constants.
# Max reviews pages to crawl.
# Reviews collected are around: 5 * MAX_REVIEWS_PAGES
MAX_REVIEWS_PAGES = 500


class TripAdvisorRestaurantBaseSpider(BaseSpider):
	name = "tripadvisor"

	allowed_domains = ["tripadvisor.com"]
	base_uri = "http://www.tripadvisor.ru"
	start_urls = [
		base_uri + "/Restaurant_Review-g60763-d12015308-Reviews-Royal_35_Steakhouse-New_York_City_New_York.html"
		#base_uri + "/RestaurantSearch?geo=60763&q=New+York+City%2C+New+York&cat=&pid="
	]


	# Entry point for BaseSpider.
	# Page type: /RestaurantSearch
	def parse(self, response):
		tripadvisor_items = []

		sel = Selector(response)
		print(sel)
		print("WTF")
		snode_restaurant = sel.xpath('//div[@id="taplc_location_detail_above_the_fold_restaurants_0"]')
		print(snode_restaurant.extract())
		print("WTF")

		tripadvisor_item = TripAdvisorItem()

		#tripadvisor_item['feedbacks_count'] = get_parsed_string(snode_restaurant, 'div[@class= "rating_and_popularity"]')
		#/span/a[@class="property_title "]/@href')
		#extracted_list = hxs.select(xpath).extract()
		sel2 = Selector(text = snode_restaurant[0].extract())
		tripadvisor_item['name'] = sel2.xpath('//h1/text()').extract_first()
		tripadvisor_item['feedbacks_count'] = sel2.xpath('//div[@class= "rating_and_popularity"]/span/div/a[@class="more"]/span/text()').extract_first()

		tripadvisor_item['pos_number'] = clean_parsed_string(sel2.xpath('//div[@class= "rating_and_popularity"]/span[2]/div/span/b/span/text()').extract_first())
		
		tripadvisor_item['href_city'] = sel2.xpath('//div[@class= "rating_and_popularity"]/span[2]/div/span/a/@href').extract_first()
		tripadvisor_item['href_city_text'] = sel2.xpath('//div[@class= "rating_and_popularity"]/span[2]/div/span/a/text()').extract_first()
		tripadvisor_item['field_with_ssss'] = sel2.xpath('//div[@class= "rating_and_popularity"]/span[3]/text()').extract_first()
		tripadvisor_item['street_address'] = sel2.xpath('//div[@class= "prw_rup prw_common_atf_header_bl headerBL"]/div/div/span[@class="street-address"]/text()').extract_first()
		tripadvisor_item['locality'] = sel2.xpath('//div[@class= "prw_rup prw_common_atf_header_bl headerBL"]/div/div/span[@class="locality"]/text()').extract_first()
		tripadvisor_item['phone'] = sel2.xpath('//div[@class= "blRow"]/div[@class= "blEntry phone"]/span[2]/text()').extract_first()
		 
		print("WTF2")
		print(snode_restaurant)
		print(tripadvisor_item['name'])
		print(tripadvisor_item['feedbacks_count'])
		print(tripadvisor_item['pos_number'])
		print(tripadvisor_item['href_city'])
		print(tripadvisor_item['href_city_text'])
		print(tripadvisor_item['field_with_ssss'])
		print(tripadvisor_item['street_address'])
		print(tripadvisor_item['locality'])
		print(tripadvisor_item['phone'])
		print("WTF2")

		yield tripadvisor_item
		





		