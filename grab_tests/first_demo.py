# coding: utf8

from grab import Grab
import json

if __name__ == '__main__':
    g = Grab()

    euro_currency = g.doc.select("//td[@id='EURUSD']/a/div[@class='index']/span[@class='mValue']/span")

    # проверяем существование этого тега
    if euro_currency.exists():
        euro_currency = euro_currency.text()

        # чертов windows
        print(euro_currency)