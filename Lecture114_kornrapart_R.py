from datetime import datetime

from forex_python.converter import CurrencyRates, get_currency_name


def currency_convert():
    print("Currency Converter From Now".center(50,"-"))
    c_convert = CurrencyRates()
    result = c_convert.get_rate(input('Which Currency would you like to convert : '), input('to : '))
    print(result)

def currency_value_at_that_time ():
    print("Currency Converter From Past".center(50,"-"))
    c_currency_value_at_that_time = CurrencyRates()
    date_currency = datetime(int(input('Year : ')), int(input('Month : ')), int(input('Date : ')), )
    currency_value = c_currency_value_at_that_time.get_rate(input('Which Currency would you like to convert : '), input('to : '),date_currency)
    print(currency_value)

def currency_calculator():
    print("How much Currency Increases or Decreases From Past".center(50,"-"))
    c_currency_calculator = CurrencyRates()
    currency_variable_1 = input('Which Currency would you like to convert : ')
    currency_variable_2 = input('to : ')
    currency_value_now_and_past = c_currency_calculator.get_rate(currency_variable_1,currency_variable_2,datetime(int(input('Year : ')), int(input('Month : ')), int(input('Date : ')), ))
    currency_value_per_year = ((c_currency_calculator.get_rate(currency_variable_1,currency_variable_2)-currency_value_now_and_past)/currency_value_now_and_past)*100
    print(currency_value_per_year.__round__(2),"%")


print("Menu Select".center(30, "-"))

print("1. Currency Converter From Now")
print("2. Currency Converter From Past")
print("3. How much Currency Increases or Decreases From Past")

print("-".center(30, "-"))
selectMenu = input("Select an option : ")
if selectMenu == "1": currency_convert()
elif selectMenu == "2": currency_value_at_that_time ()
elif selectMenu == "3": currency_calculator()