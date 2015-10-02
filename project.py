import web_utility

amount = str('5')
first_country = 'EUR'
sec_country = 'USD'

url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"

url_string = url_string.replace('1', amount)
url_string = url_string.replace('AUD', first_country)
url_string = url_string.replace('JPY', sec_country)


print (url_string)

result = web_utility.load_page(url_string)
print(result[result.index('result'):])
url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"
