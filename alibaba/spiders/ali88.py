# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from alibaba.items import companyItem
from alibaba.starturls import starturls
from urlparse import urlparse,parse_qs
from urllib import urlencode
from bs4 import BeautifulSoup

company_m_page_template = "http://m.1688.com/winport/company/{0}.html"

locale={
    u"公司名称":"company_name",
    u"经营模式":"business_mode",
    u"所在地区":"company_region",
    u"主营产品":"main_product",
    u"商品数量":"recordsof_goods",
    u"供应等级":"supply_grade",
    u"交易勋章":"trade_medal",
    u"满意度 ":"customer_satisfaction",
    u"联系人 ":"contact_person",
    u"联系地址":"contact_address",
    u"经营地址":"company_address",
    u"成立日期":"established_time",
    u"经营范围":"business_scope",
    u"注册号":"registation_number",
    u"法人代表":"corporate_representative",
    u"企业类型":"company_type",
    u"营业期限":"allotted_time",
    u"登记机关":"registration_authority",
    u"详情网页":"companyprofile_url"
}

class Ali88Spider(scrapy.Spider):
    name = "ali88"
    start_urls = starturls
    def parse(self,response):
         company_link=response.xpath('//div[@class="item"]/a/@href').extract()
         for url in company_link:
            b2bID=re.search("(?<=/winport/).*?(?=\.html)",url).group()
            yield scrapy.Request(company_m_page_template.format(b2bID),callback=self.parse_info)  
            if len(company_link):
                qs= parse_qs(urlparse(response.url).query)
                flat_qs=dict()
                [flat_qs.setdefault(k,v) for k,vlist in qs.iteritems() for v in vlist]
                if "beginPage" in flat_qs:
                	flat_qs["beginPage"]=str(int(flat_qs["beginPage"])+1)
                else:
                	flat_qs["beginPage"]="2"
                yield scrapy.Request(re.search(".*?html",response.url).group()+"?{0}".format(urlencode(flat_qs)))
                qs=dict()
        
    def parse_info(self,response):
        l=ItemLoader(item=companyItem(),response=response)
        soup = BeautifulSoup(response.body,"lxml")
        divs = soup.find_all(class_='info-container') 
        for div in divs:
            em = div.find("em")
            if em:
                fieldName=re.sub('\s','',em.get_text())
                fieldName=re.sub(':','',fieldName)
                span = div.find("span")
                img = div.find('img') 
                if span:
                    span ="".join(span.stripped_strings)
                    span = re.sub('\s','',span)

                    if fieldName in locale:  
                        l.add_value(locale[fieldName],span)
                elif img and not img.has_attr('class'):
                    img = img.get("src")
                    img = re.search('(?<=sale_)\d\w+',img) or re.search('(?<=icon/)\w+',img)
                    img=img.group()
                    if fieldName in locale:
                        l.add_value(locale[fieldName],img)         
                else :
                    continue    
        return l.load_item()
    