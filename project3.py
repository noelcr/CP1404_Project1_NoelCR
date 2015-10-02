from currency import Currency
conversion = Currency()
converted_money = conversion.convert('10', 'EUR', 'AUD')

countrypro = Currency()
countrypro.get_details('Australia')