# dictionary: of price of stock prices
stock_price = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 140,
    "MSFT" : 330,
    "AMZN" : 130
}
# Dict to hold user's entered portfolio
user_portfolio = {}
print("Welcome to the STOCK PORTFOLIO TRACKER!")
print(f"Availabe stocks: {', '.join(stock_price.keys())}")
# input / output and oop: get data from user
while True:
    print("-"*30)
    symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if symbol == 'DONE' :
        break
    if symbol not in stock_price:
        print("Stock not found. Please choose from the available list. ")
        continue
    # get the quantity and ensure it's a valid number
    quantity_input = input(f"Enter the number of shares you own for {symbol}: ")
    if not quantity_input.replace('.', '',1).isdigit():
        print("Invalid input. Please enter a number.")
        continue
    quantity = float(quantity_input)

    # add or update the quantity in the user's portfolio
    if symbol in user_portfolio:
        user_portfolio[symbol] += quantity
    else :
        user_portfolio[symbol] = quantity
print("\nCalculating your portfolio value....")
total_investment = 0.0
summer_lines = [] # I store the text here so we can print it and save it.
summer_lines.append("=== PORTFOLIO SUMMERY ===")
# calculate values 
for symbol, qty in user_portfolio.items():
    price = stock_price[symbol]
    # basic arithmetic: multiply quantity price 
    value = qty * price
    total_investment += value
    # format the line to look clean (AARL: 5.0 shares - 180 = 900 )
    summer_lines.append(f"{symbol}: {qty} shares @ ${price} = ${value}")
summer_lines.append("-"*25)
summer_lines.append(f"TOTAL INVESTMENT VALUE : ${total_investment}")
summer_lines.append("=====================")
# FILE HANDLING - write results to a .txt file
filename = "portfolio_summery.txt"
# 'w' mode opens file for working (and creates it if it doesn't exist)
with open(filename, 'w') as file:
    for line in summer_lines:
        print(line)
        file.write(line + "\n")
print(f"\nSuccess your report has been saved to {filename}")