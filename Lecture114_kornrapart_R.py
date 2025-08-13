from datetime import datetime

from forex_python.converter import CurrencyRates, get_currency_name


def currencyConvert():
    print("Currency Converter From Now".center(50,"-"))
    cConvert = CurrencyRates()
    result = cConvert.get_rate(input('Which Currency would you like to convert : '), input('to : '))
    print(result)

def currencyValueAtThatTime ():
    print("Currency Converter From Past".center(50,"-"))
    cCurrencyValueAtThatTime = CurrencyRates()
    dateCurrency = datetime(int(input('Year : ')), int(input('Month : ')), int(input('Date : ')), )
    currencyValue = cCurrencyValueAtThatTime.get_rate(input('Which Currency would you like to convert : '), input('to : '),dateCurrency)
    print(currencyValue)

def currencyCalculator():
    print("How much Currency Increases or Decreases From Past".center(50,"-"))
    cCalculator = CurrencyRates()
    currencyVariable1 = input('Which Currency would you like to convert : ')
    currencyVariable2 = input('to : ')
    currencyValueNowAndPast = cCalculator.get_rate(currencyVariable1,currencyVariable2,datetime(int(input('Year : ')), int(input('Month : ')), int(input('Date : ')), ))
    currencyValuePerYear = ((cCalculator.get_rate(currencyVariable1,currencyVariable2)-currencyValueNowAndPast)/currencyValueNowAndPast)*100
    print(currencyValuePerYear.__round__(2),"%")


print("Menu Select".center(30, "-"))

print("1. Currency Converter From Now")
print("2. Currency Converter From Past")
print("3. How much Currency Increases or Decreases From Past")

print("-".center(30, "-"))
selectMenu = input("Select an option : ")
if selectMenu == "1": currencyConvert()
elif selectMenu == "2": currencyValueAtThatTime()
elif selectMenu == "3": currencyCalculator()