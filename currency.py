import re
class Currency():

    def __init__(self,amount="", home_currency_code="", location_currency_code=""):
        self.amount=amount
        self.home_currency_code=home_currency_code
        self.location_currency_code=location_currency_code

    def convert(self):
        import web_utility

        url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"

        url_string = url_string.replace('1', self.amount)
        url_string = url_string.replace('AUD', self.home_currency_code)
        url_string = url_string.replace('JPY', self.location_currency_code)


        if self.home_currency_code == self.location_currency_code:
            #print("-1")
            return -1.00, "Invalid Conversion"
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
        #regular expression
        #/d+ - any number, one or more

        #print(conversion_num)
        final_conversion_num = conversion_num[1]
        #print(final_conversion_num)

        return final_conversion_num, "Valid conversion"






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
                pass

        c_details.close()
        country_tuple = ()
        return country_tuple


conversion = Currency('10', 'AUD', 'USD')
print("{}   {}  {}->{}  {}".format(conversion.convert()[1],   conversion.amount,  conversion.home_currency_code,conversion.location_currency_code,   conversion.convert()[0]))
conversion = Currency('10', 'AUD', 'EUR')
print("{}   {}  {}->{}  {}".format(conversion.convert()[1],   conversion.amount,  conversion.home_currency_code,conversion.location_currency_code,   conversion.convert()[0]))
conversion = Currency('1', 'AUD', 'AUD')
print("{}   {}  {}->{}  {}".format(conversion.convert()[1],   conversion.amount,  conversion.home_currency_code,conversion.location_currency_code,   conversion.convert()[0]))

test_currency = Currency()
print(test_currency.get_details('Australia'))
