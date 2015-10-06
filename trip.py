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
        print(symbol_list)
        amount =  10
        print(symbol_list[-1],amount)
    def __str__(self,name,currency_code,currency_symbol):
        print("{}, {}, {}").format(name, currency_code, currency_symbol)



    def display_symbol(self, money_amount=0):
        print()



class Details():
    print()




Country('Germany', 'EUR', '€')

