from datetime import datetime


class Error(Exception):
    def Error(self, value):
        super().__init__(value)

class Country():
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        # print(name, currency_code, currency_symbol)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.currency_code, self.currency_symbol)

    def symbol_assign_to_amount(self, amount):
        return '{}{}'.format(self.currency_symbol, amount)


class Details():
    def __init__(self, country_name="", start_date="", end_date=""):
        self.locations = []
        self.country_name = country_name
        self.start_date = start_date
        self.end_date = end_date

    def add(self):
        # print(self.country_name)
        # print(self.start_date)
        # print(self.end_date)
        first_date = datetime.strptime(self.start_date, '%Y/%m/%d')
        first_date = datetime.date(first_date)
        # print(first_date)
        self.first_date2 = first_date
        #print(self.first_date2)
        #
        sec_date = datetime.strptime(self.end_date, '%Y/%m/%d')
        sec_date = datetime.date(sec_date)
        # print(sec_date)
        self.sec_date2 = sec_date
        #print(self.sec_date2)

        if self.first_date2 > self.sec_date2:
            raise Error('Your first date was after the second date')
        else:
            if self.start_date in self.locations:
                raise Error('Date already used')
            else:
                self.locations.append(self.country_name)
                self.locations.append(self.start_date)
                self.locations.append(self.end_date)

        # print(self.locations)
        return self.locations

    def current_country(self, date_string=""):
        date_string = datetime.strptime(date_string, '%Y/%m/%d')
        date_string = datetime.date(date_string)
        if date_string > self.first_date2 and date_string < self.sec_date2:
            return self.country_name
            # print(self.country_name)
        else:
            raise Error("Date not within a trip")

    def is_empty(self):
        if not self.locations:
            return True
        else:
            return False

test_country1 = Country('makeupland', 'BNL', '€')
print(test_country1.symbol_assign_to_amount('10'))
print(test_country1)#tests for the overloaded __str__ function



testing = Details('Germany', '1997/01/25', '1997/01/29')
print(testing.add())

testing.current_country("1997/01/27")
print(testing.is_empty())#True if empty, #False if not

