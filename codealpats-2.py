# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 320
}

# Ask how many different stocks user owns
num_stocks = int(input("How many different stocks do you have? "))

total_value = 0

# Loop to collect each stock and quantity
for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"How many shares of {stock_name}? "))

    if stock_name in stock_prices:
        stock_value = stock_prices[stock_name] * quantity
        total_value += stock_value
        print(f"{stock_name}: ${stock_prices[stock_name]} × {quantity} = ${stock_value}")
    else:
        print(f"Sorry, we don't have a price for {stock_name}.")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_value}")
    print("Result saved to portfolio_summary.txt")
