#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
from recipe_scrapers import scrap_me

try:
    scrap_me = scrap_me('https://www.budgetbytes.com/2017/07/slow-cooker-sesame-beef/')
    pprint(scrap_me.data())
except KeyError:
    print "Website is not supported."
