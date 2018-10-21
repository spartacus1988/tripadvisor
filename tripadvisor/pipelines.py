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



		# value = header[0] +' varchar(250), ' + header[1] + ' int , ' + header[2] +' int );'


		# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

		value = """"id INT(11) NOT NULL AUTO_INCREMENT, 
					name VARCHAR(255) NOT NULL,
					feedbacks_count VARCHAR(255) NOT NULL,
					pos_number VARCHAR(255) NOT NULL,
					href_city VARCHAR(255) NOT NULL,
					href_city_text VARCHAR(255) NOT NULL,
					field_with_ssss VARCHAR(255) NOT NULL,
					street_address VARCHAR(255) NOT NULL,
					locality VARCHAR(255) NOT NULL,
					phone VARCHAR(255) NOT NULL,
					PRIMARY KEY(id)"""

		# STRING = 'CREATE TABLE IF NOT EXISTS ' + TABLE_NM + '( ' 
		# 			+ 'id INT(11) NOT NULL AUTO_INCREMENT, '  
		# 			+ 'name VARCHAR(255) NOT NULL, '
		# 			+ 'feedbacks_count VARCHAR(255) NOT NULL, '
		# 			+ 'pos_number VARCHAR(255) NOT NULL, '
		# 			+ 'href_city VARCHAR(255) NOT NULL, '
		# 			+ 'href_city_text VARCHAR(255) NOT NULL, '
		# 			+ 'field_with_ssss VARCHAR(255) NOT NULL, '
		# 			+ 'street_address VARCHAR(255) NOT NULL, '
		# 			+ 'locality VARCHAR(255) NOT NULL, '
		# 			+ 'phone VARCHAR(255) NOT NULL, '
		# 			+ 'PRIMARY KEY(id)' + ' )' 


		# STRING = ('CREATE TABLE IF NOT EXISTS ' + TABLE_NM + '( ' 
		# 			+ 'id INT(11) NOT NULL AUTO_INCREMENT, '  
		# 			+ 'name VARCHAR(255) NOT NULL, '
		# 			+ 'feedbacks_count VARCHAR(255) NOT NULL, '
		# 			+ 'pos_number VARCHAR(255) NOT NULL, '
		# 			+ 'href_city VARCHAR(255) NOT NULL, '
		# 			+ 'href_city_text VARCHAR(255) NOT NULL, '
		# 			+ 'field_with_ssss VARCHAR(255) NOT NULL, '
		# 			+ 'street_address VARCHAR(255) NOT NULL, '
		# 			+ 'locality VARCHAR(255) NOT NULL, '
		# 			+ 'phone VARCHAR(255) NOT NULL, '
		# 			+ 'PRIMARY KEY(id)' + ' )')


		STRING= ( "CREATE TABLE IF NOT EXISTS " + TABLE_NM + "( "
			    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
			    "  `name` VARCHAR(255) NOT NULL,"
			    "  `feedbacks_count` VARCHAR(255) NOT NULL,"
			    "  `pos_number` VARCHAR(255) NOT NULL,"
			    "  `href_city` VARCHAR(255) NOT NULL,"
			    "  `href_city_text` VARCHAR(255) NOT NULL,"
			    "  `field_with_ssss` VARCHAR(255) NOT NULL,"
			    "  `street_address` VARCHAR(255) NOT NULL,"
			    "  `locality` VARCHAR(255) NOT NULL,"
			    "  `phone` VARCHAR(255) NOT NULL,"
			    "  PRIMARY KEY (`id`)"
			    ")"
			    )

		print(STRING)

		if result_table == 0:
			#self.cursor.execute('CREATE TABLE IF NOT EXISTS ' + TABLE_NM + '( ' + value + ' )')
			self.cursor.execute(STRING)
			return 0
		else:
			self.cursor.execute('DROP TABLE ' + TABLE_NM + ';')
			self.create_table(TABLE_NM)



	def process_item(self, item):    
		try:
			#self.cursor.execute("INSERT INTO "+ TABLE_NM + " VALUES (' " + tbody[k-1] +"',"+tbody[k] +","+tbody[k+1] + " );")
			self.cursor.execute("INSERT INTO "+ TABLE_NM + " VALUES (' " + item['name'] +"',"
				+ item['feedbacks_count'] + "," 
				+ item['pos_number'] + ","
				+ item['href_city'] + ","
				+ item['href_city_text'] + ","
				+ item['field_with_ssss'] + ","
				+ item['street_address'] + ","
				+ item['locality'] + ","
				+ item['phone'] + ","
				+ " );")

			self.conn.commit()            
		except MySQLdb.Error as e:
			print(e)




class TripadvisorPipeline(object):
	def process_item(self, item, spider):
		return item
