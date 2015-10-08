# class Error():
#     try:
#         print(1 / 1)
#     except ZeroDivisionError as error:
#         print(error)
#     print("After try/except")


class Country():
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        print(name, currency_code, currency_symbol)
        #print(currency_symbol)


    def __str__(self):
        return "{}, {}, {}".format(self.name, self.currency_code, self.currency_symbol)


    def symbol_assign(self, amount):
        #print(self.currency_symbol, "test")
        #amount = 10#int(input("amount: "))
        print('{}{}'.format(self.currency_symbol, amount))




class Details():
    def __init__(self):
        self.locations = []

    def add(self, country_name="", start_date="", end_date=""):
        #print("A date string conforms to this format: YYYY/MM/DD")
        return country_name, start_date, end_date

    def current_country(self, date_string):
        print()

    def is_empty(self):
        print()

#Country('Germany', 'EUR', '€')
#print(Country)#why doesn't this work?


test_country1 = Country('bananaland', 'BNL', '€')


# test_details = Details.add(Details, 'Germany', '1997/01/25', '1997/01/30')
# print(test_details)


test_country1.symbol_assign('10')