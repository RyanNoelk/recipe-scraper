## Recipe scrapers

[![Build Status](https://travis-ci.org/hhursev/recipe-scraper.svg?branch=master)](https://travis-ci.org/hhursev/recipe-scraper)

A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package.

    pip install git+git://github.com/RyanNoelk/recipe-scraper.git@1.0.6

then:

    from recipe_scrapers import scrap_me

    # give the url as a string, it can be url from any site listed below
    try:
        scrap_me = scrap_me('https://www.budgetbytes.com/2017/03/lemon-garlic-roasted-chicken')
        print(scrap_me.data())
    except KeyError:
        print 'Website is not supported.'


### Contribute

Part of the reason I want this open sourced is because if a site makes a design change, the scraper
for it should be modified.

If you spot a design change (or something else) that makes the scrapers unable to work for the given
site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer
 :beer:.


### Scrapers available for:

- [http://allrecipes.com/](http://allrecipes.com/)
- [http://budgetbytes.com/](http://budgetbytes.com/)
- [http://pamperedchef.com/](http://pamperedchef.com/)
- [http://tasteofhome.com/](http://tasteofhome.com/)
