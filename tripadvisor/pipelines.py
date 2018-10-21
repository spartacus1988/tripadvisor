# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import os
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request


HOST_DB = 'localhost'
USER_DB = os.getlogin() 
PASSWD_US = 'password'
NAME_DB = 'testdb'
TABLE_NM = 'test_table'


class MySQLStorePipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect(HOST_DB, USER_DB, PASSWD_US, 
									charset="utf8",
									use_unicode=True)
		self.cursor = self.conn.cursor()
		sql = 'CREATE DATABASE IF NOT EXISTS '+ NAME_DB + ' CHARACTER SET utf8 COLLATE utf8_unicode_ci;'
		self.cursor.execute(sql)
		self.cursor.execute('use ' + NAME_DB)
		self.create_table(TABLE_NM)



	def create_table(self, TABLE_NM):
		result_table = self.cursor.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = "' + NAME_DB + '" AND table_name = "'+ TABLE_NM +'";')
		STRING= ( "CREATE TABLE IF NOT EXISTS " + TABLE_NM + "( "
			    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
			    "  `name` VARCHAR(255) NOT NULL,"
			    "  `feedbacks_count` VARCHAR(255) NOT NULL,"
			    "  `pos_number` TEXT NOT NULL,"
			    "  `href_city` TEXT NOT NULL,"
			    "  `href_city_text` TEXT NOT NULL,"
			    "  `field_with_ssss` TEXT NOT NULL,"
			    "  `street_address` TEXT NOT NULL,"
			    "  `locality` TEXT NOT NULL,"
			    "  `phone` VARCHAR(255) NOT NULL,"
			    "  PRIMARY KEY (`id`)"
			    ")"
			    )

		#print(STRING)

		if result_table == 0:
			self.cursor.execute(STRING)
			return 0
		else:
			self.cursor.execute('DROP TABLE ' + TABLE_NM + ';')
			self.create_table(TABLE_NM)



	def process_item(self, item):    
		try:
			add_restaurant = ("INSERT INTO "+ TABLE_NM + " "
               "(name, feedbacks_count, pos_number, href_city, href_city_text, field_with_ssss, street_address, locality, phone) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
			data_restaurant = (item['name'], item['feedbacks_count'], item['pos_number'], item['href_city'], 
				item['href_city_text'], item['field_with_ssss'], item['street_address'], item['locality'], item['phone'])

			# Insert new restaurant
			self.cursor.execute(add_restaurant, data_restaurant)
			self.conn.commit()            
		except MySQLdb.Error as e:
			print(e)

	def show_item(self):
		try:
			query = ('select * from '+ TABLE_NM )

			self.cursor.execute(query)
			output = self.cursor.fetchall()

			for row in output:
				print (row)

		except MySQLdb.Error as e:
			print(e)




class TripadvisorPipeline(object):
	def process_item(self, item, spider):
		return item
