"""7% Investment Return"""

principal = 1000
rate_of_return = 7

no_of_years = int(input('Enter number of years: '))

amount_on_deposit = principal * (1 + rate_of_return) ** no_of_years

print("The money remaining at the end of", no_of_years, "years is $", amount_on_deposit)
