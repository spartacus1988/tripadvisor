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
		#print("WTF")
		snode_restaurant = sel.xpath('//div[@id="taplc_location_detail_above_the_fold_restaurants_0"]')
		#print(snode_restaurant.extract())
		#print("WTF")
		tripadvisor_item = TripAdvisorItem()

		sel2 = Selector(text = snode_restaurant[0].extract())
	
		tripadvisor_item['name'] = clean_parsed_string(get_parsed_string(sel2, '//h1/text()'))
		tripadvisor_item['feedbacks_count'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "rating_and_popularity"]/span/div/a[@class="more"]/span/text()'))
		tripadvisor_item['pos_number'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "rating_and_popularity"]/span[2]/div/span/b/span/text()'))
		tripadvisor_item['href_city'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "rating_and_popularity"]/span[2]/div/span/a/@href'))
		tripadvisor_item['href_city_text'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "rating_and_popularity"]/span[2]/div/span/a/text()'))
		tripadvisor_item['field_with_ssss'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "rating_and_popularity"]/span[3]/text()'))
		tripadvisor_item['street_address'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "prw_rup prw_common_atf_header_bl headerBL"]/div/div/span[@class="street-address"]/text()'))
		tripadvisor_item['locality'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "prw_rup prw_common_atf_header_bl headerBL"]/div/div/span[@class="locality"]/text()'))
		tripadvisor_item['phone'] = clean_parsed_string(get_parsed_string(sel2, '//div[@class= "blRow"]/div[@class= "blEntry phone"]/span[2]/text()'))

		 
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
		





		