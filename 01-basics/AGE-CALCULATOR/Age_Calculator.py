# Age Calculator
from datetime import datetime
print("--------lets calculate your age---------")

current_year = datetime.now().year
year = int(input("\nEnter you year of Birth in format (20xx)"))

age = current_year - year

print("Your age is ",age,"in ",current_year)