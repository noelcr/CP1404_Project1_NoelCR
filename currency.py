import re
class Currency():

    def __init__(self,amount=0, home_currency_code='', location_currency_code=''):
        self.amount=0
        self.home_currency_code=""
        self.location_currency_code=""

    def convert(self, amount, home_currency_code, location_currency_code):
        import web_utility

        url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"

        url_string = url_string.replace('1', amount)
        url_string = url_string.replace('AUD', home_currency_code)
        url_string = url_string.replace('JPY', location_currency_code)


        if home_currency_code == location_currency_code:
            print("-1")
            return -1
        else:
            print()

        result = web_utility.load_page(url_string)
        #print(result[result.index('result'):])
        store_result = result[result.index('result'):]
        #print(store_result)
        url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"

        new_store_result = store_result.replace('\\n', "")
        #print(new_store_result)

        conversion_num = (re.findall('\d+(?:\.\d+)?', new_store_result))
        #print(conversion_num)
        final_conversion_num = conversion_num[1]
        print(final_conversion_num)
        return final_conversion_num






    def get_details(self, country_name):
        c_details = open('currency_details.txt', 'r')
        country_tuple = ()
        for line in c_details:
            if country_name in line:
                #print("found")
                #print(line)
                country_tuple = line
                return country_tuple
            else:
                country_tuple = ()
        c_details.close()
        print()


conversion = Currency()
converted_money = conversion.convert('10', 'EUR', 'AUD')

print(converted_money)
countrypro = Currency()
print(countrypro.get_details('Australia'))