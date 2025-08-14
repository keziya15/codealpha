# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,  # Apple
    "TSLA": 250,  # Tesla
    "GOOG": 2700, # Google
    "MSFT": 300,  # Microsoft
    "AMZN": 3500  # Amazon
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not available in our list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    investment_value = stock_prices[stock_name] * quantity
    total_investment += investment_value
    print(f"✅ Added {quantity} shares of {stock_name} worth ${investment_value}")

# Display results
print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - {qty} shares - Value: ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save portfolio to file? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} - {qty} shares - Value: ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("📂 Portfolio saved to portfolio.txt")