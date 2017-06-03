#!/usr/bin/env python
# encoding: utf-8

from fractions import Fraction
from ._abstract import AbstractScraper
from ._utils import normalize_string


class BudgetBytesv2(AbstractScraper):

    @classmethod
    def host(self):
        return 'budgetbytes.com-v2'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return {
            'prep-time': self.soup.find(
                'span',
                {'class': 'wprm-recipe-prep_time-minutes'}
            ).get_text(),
            'cook-time': self.soup.find(
                'span',
                {'class': 'wprm-recipe-cook_time-minutes'}
            ).get_text()
        }

    def servings(self):
        return self.soup.find('span', {'itemprop': 'recipeYield'}).get_text().split(' ', 1)[0]

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': 'wprm-recipe-ingredient'})
        ingredients = []

        for ingredient in ingredients_html:
            try:
                ingredient_dict = {
                    'quantity': round(float(sum(Fraction(s) for s in ingredient.find(
                        'span',
                        {'class': 'wprm-recipe-ingredient-amount'}
                    ).get_text().split())), 3),
                    'measurement': ingredient.find(
                        'span',
                        {'class': 'wprm-recipe-ingredient-unit'}
                    ).get_text(),
                    'title': ingredient.find(
                        'span',
                        {'class': 'wprm-recipe-ingredient-name'}
                    ).get_text()
                }
            except AttributeError:
                ingredient_dict = {
                    'title': ingredient.find(
                        'span',
                        {'class': 'wprm-recipe-ingredient-name'}
                    ).get_text()
                }
            except:
                ingredient_dict = {
                    'title': ingredient
                }

            ingredients.append(ingredient_dict)

        return ingredients

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'class': 'wprm-recipe-instruction'})

        return [
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ]

    def description(self):
        li = self.soup.find('article', {'class': 'post'}).findAll('p')
        return li[0].get_text()

    def image(self):
        return self.soup.find('img', {'class': 'alignnone'})["src"]
