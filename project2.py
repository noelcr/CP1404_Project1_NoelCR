c_details = open('currency_details.txt', 'r')


country_name = str(input("enter country: "))
country_tuple = ()
for line in c_details:
    if country_name in line:
        #print("found")
        print(line)
        country_tuple = line
        print(country_tuple)
c_details.close()


