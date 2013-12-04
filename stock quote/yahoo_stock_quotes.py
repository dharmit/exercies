#!/usr/bin/env python
import requests

# API string found on http://www.gummy-stuff.org/Yahoo-data.htm

def get_quote(stock_symbol):

    api = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=sl1" % stock_symbol
    api_request = requests.get(api)
    quote = api_request.content.split(',')
    
    print "%s - %s" % (quote[0], quote[1])

if __name__ == "__main__":
    
    company = raw_input("Enter the company symbol (eg: RHT, GOOG, AAPL): ") 
    get_quote(company)
