c_details = open('currency_details.txt', 'r')


country = str(input("enter country: "))

for line in c_details:
    if country in line:
        print("found")



c_details.close()