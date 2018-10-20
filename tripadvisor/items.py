# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TripAdvisorItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	#pass
	
	name = scrapy.Field()
	feedbacks_count = scrapy.Field()
	pos_number = scrapy.Field()
	href_city = scrapy.Field()
	href_city_text = scrapy.Field()
	field_with_ssss = scrapy.Field()
	street_address = scrapy.Field() 
	locality = scrapy.Field() 
	phone = scrapy.Field() 
