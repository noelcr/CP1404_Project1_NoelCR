class Error():
    try:
        print(1/1)
    except ZeroDivisionError as error:
        print(error)
    print("After try/except")

class Country():
    def __init__(self, name, currency_code, currency_symbol):
        self.name=""
        self.currency_code=""
        self.currency_symbol=""
        print(name, currency_code, currency_symbol)
        symbol_list = []
        symbol_list.append(name)
        symbol_list.append(currency_code)
        symbol_list.append(currency_symbol)
        #print(symbol_list)
        amount =  int(input("amount: "))
        print('{}{}'.format(symbol_list[-1],amount))

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.currency_code, self.currency_symbol)


class Details:
    def __init__(self):
        self.locations = []

    def add(self, country_name="", start_date="", end_date=""):
        print("A date string conforms to this format: YYYY/MM/DD")
        self.country_name=""
        self.start_date=""
        self.end_date=""
        print(self.country_name, self.start_date, self.end_date)

Country('Germany', 'EUR', '€')
#print(Country)#why doesn't this work?


