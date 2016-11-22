# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import TakeFirst    
class companyItem(scrapy.Item):
    company_name = scrapy.Field(output_processor=TakeFirst())
    business_mode = scrapy.Field(output_processor=TakeFirst())
    company_region = scrapy.Field(output_processor=TakeFirst())
    main_product = scrapy.Field(output_processor=TakeFirst())
    recordsof_goods = scrapy.Field(output_processor=TakeFirst())
    supply_grade = scrapy.Field(output_processor=TakeFirst())
    trade_medal = scrapy.Field(output_processor=TakeFirst())
    customer_satisfaction = scrapy.Field(output_processor=TakeFirst())
    contact_person=scrapy.Field(output_processor=TakeFirst())
    contact_address = scrapy.Field(output_processor=TakeFirst())
    company_address = scrapy.Field(output_processor=TakeFirst())
    established_time = scrapy.Field(output_processor=TakeFirst())
    business_scope = scrapy.Field(output_processor=TakeFirst())
    registation_number = scrapy.Field(output_processor=TakeFirst())
    corporate_representative=scrapy.Field(output_processor=TakeFirst())
    company_type = scrapy.Field(output_processor=TakeFirst())
    allotted_time = scrapy.Field(output_processor=TakeFirst())
    registration_authority = scrapy.Field(output_processor=TakeFirst())
    companyprofile_url = scrapy.Field(output_processor=TakeFirst())