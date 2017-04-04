#!/usr/bin/env python
# encoding: utf-8

from recipe_scrapers import scrap_me

# give the url as a string, it can be url from any site listed below
scrap_me = scrap_me('https://www.budgetbytes.com/2017/03/lemon-garlic-roasted-chicken')

# print(scrap_me.title())
# print(scrap_me.servings())
# print(scrap_me.total_time())
print(scrap_me.ingredients())
# print(scrap_me.instructions())
# print(scrap_me.description())
# print(scrap_me.image())
