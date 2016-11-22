# -*- coding: utf-8 -*-
from loc import province
from categroies import categroies
search_company="http://m.1688.com/page/search.html?type=company&keywords={0}&province={1}"
search_company_city="http://m.1688.com/page/search.html?type=company&keywords={0}&province={1}&city={2}"
starturls=list()
prefix="http://m.1688.com/page/search.html?type=company&keywords="
for p in province:
	if p["name"] in {"北京","上海","重庆","天津"}:
		for keywords in categroies:
			starturls.append(search_company.format(keywords,p["name"]))
	else:
		for city in p["city"]:
			for keywords in categroies:
				starturls.append(search_company_city.format(keywords,p["name"],city["name"]))