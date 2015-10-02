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

        result = web_utility.load_page(url_string)
        print(result[result.index('result'):])
        url_string = "https://www.google.com/finance/converter?a=1&from=AUD&to=JPY"


    def get_details(self, country_name):
        c_details = open('currency_details.txt', 'r')
        country_tuple = ()
        for line in c_details:
            if country_name in line:
                #print("found")
                print(line)
                country_tuple = line

        c_details.close()
        print()


# variable_name = Currency()
# variable_name.convert('5', 'USD', 'AUD')

# countrypro = Currency()
# countrypro.get_details('Australia')