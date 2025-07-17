Question 2: Currency Converter (20 points)
 
Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:
 
Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used

choice = input("1 THB -> USD, 2 USD -> THB: ")
amount = float(input("amount: "))
if choice == "1":
    print(f"{amount}THB = {amount/35.5}USD")
if choice == "2":
    print(f"{amount}USD = {amount" 35.5}THB")