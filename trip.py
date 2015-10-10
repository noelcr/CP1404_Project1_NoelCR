from datetime import datetime


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
        # print(currency_symbol)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.currency_code, self.currency_symbol)

    def symbol_assign_to_amount(self, amount):
        # print(self.currency_symbol, "test")
        # amount = 10#int(input("amount: "))
        return '{}{}'.format(self.currency_symbol, amount)


# ##Country('Germany', 'EUR', '€')
# test_country1 = Country('bananaland', 'BNL', '€')
# print(test_country1.symbol_assign_to_amount('10'))
# print(test_country1)#tests for the overloaded __str__ function


class Details():
    def __init__(self):
        self.locations = []

    def add(self, country_name="", start_date="", end_date=""):
        # print("A date string conforms to this format: YYYY/MM/DD")
        # WHERE DATE CHECKING GOES ----> ADD EXCEPTIONS
        first_date = datetime.strptime(start_date, '%Y/%m/%d')
        first_date = datetime.date(first_date)
        # print(first_date)

        sec_date = datetime.strptime(end_date, '%Y/%m/%d')
        sec_date = datetime.date(sec_date)
        # print(sec_date)

        if first_date > sec_date:
            raise ValueError('Your first date was after the second date')
        else:
            if start_date in self.locations:
                raise Exception('Date already used')
            else:
                self.locations.append(country_name)
                self.locations.append(first_date)
                self.locations.append(sec_date)


        ##########this belongs in current_country function, however not working atm################## IT WORKS
        ###find how to get these varaibles into the current country function###
        date_string = datetime.strptime('2000/01/15', '%Y/%m/%d')
        date_string = datetime.date(date_string)
        if date_string > first_date and date_string < sec_date:
            #return country_name
            print(country_name)
        else:
            print("nope")


        return self.locations

    def current_country(self, date_string):
        print()
        # if date_string > first_date and date_string < sec_date:
        #     return final_country_name
        # else:
        #     print("nope")

    def is_empty(self):
        if not self.locations:
            return False
        else:
            return True


# test_country1 = Country('bananaland', 'BNL', '€')
# print(test_country1.symbol_assign_to_amount('10'))
# print(test_country1)#tests for the overloaded __str__ function

test_details1 = Details()
print(test_details1.add('Germany', '1997/01/25', '1997/01/31'))

test_details2 = Details()
print(test_details2.add('Australia', '2000/01/01', '2000/02/01'))

# is_empty_result = Details()
# print(is_empty_result.is_empty())

# test_current_country = Details()
# print(test_current_country.current_country('2000/01/15'))
