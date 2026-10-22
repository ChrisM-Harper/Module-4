# Christopher Monarrez M4P2

# Variables
price_per_share = float(input("Enter price per share: "))
current_stock_price = float(input("Enter current stock price "))
quantity_stock = int(input("Enter quantity of stock: "))


# Calculation
stock_difference = (current_stock_price - price_per_share) * quantity_stock


# Display
print("Stock price difference: $", stock_difference)
