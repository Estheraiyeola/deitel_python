from _decimal import Decimal

gallons_total = 0
miles_total = 0
gallons = float(input('Enter the gallons used (-1 to end): '))
while gallons != -1:
    miles = int(input('Enter the miles driven: '))
    gallons_total = gallons_total + gallons
    miles_total = miles_total + miles
    miles_per_gallon = miles / gallons
    print(f'{Decimal(miles_per_gallon):.6f}')

    gallons = float(input('Enter the gallons used (-1 to end): '))
overall_miles_and_gallon = miles_total / float(gallons_total)
# print(gallons_total)
# print(miles_total)
print(f'The overall average miles/gallon was {Decimal(overall_miles_and_gallon):.6f}')

