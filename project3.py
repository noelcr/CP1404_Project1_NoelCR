from datetime import datetime
# from currency import Currency
# conversion = Currency()
# converted_money = conversion.convert('10', 'EUR', 'AUD')
#
# countrypro = Currency()
# countrypro.get_details('Australia')



date1 = '1997/01/16'
date2 = '1997/01/20'

a = datetime.strptime('1997/01/25', '%Y/%m/%d')
a = datetime.date(a)
print(a)

b = datetime.strptime('1997/09/29', '%Y/%m/%d')
b = datetime.date(b)
print(b)

if a < b:
    print("is less")
else:
    print("is greater")


