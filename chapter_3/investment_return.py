
principal = 1000
rate_of_return = 7

for no_of_years in range(1, 30):
    amount_on_deposit = principal * (1 + rate_of_return) ** no_of_years
    print("The money remaining at the end of", no_of_years, "years is $", amount_on_deposit)
