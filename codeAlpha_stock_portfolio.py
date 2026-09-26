stock_name = {
    "AAPL": 500,
    "GOOG": 700,
    "AMZN": 2000,
    "TCLS": 800,
    "PLSC": 300
}

print("Available Stocks:", ", ".join(stock_name.keys()))

total = 0
portfolio = []

while True:
    user = input("Enter stock name: ").upper()

    if user in stock_name:
        quantity = int(input("Enter quantity: "))

        stock_value = stock_name[user]
        investment = stock_value * quantity

        total = total + investment

        print(f"{user}: {quantity} shares * {stock_value} = {investment}")

        portfolio.append(
            f"{user} - {quantity} shares - {investment}"
        )

        choice = input(
            "Do you want to add another stock? (Y/N): "
        ).upper()

        if choice == "N":
            break

    else:
        print("Stock does not exist!")

print("\nTotal Investment:", total)

# Save portfolio details to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    file.write("-------------------------\n")

    for item in portfolio:
        file.write(item + "\n")

    file.write("\nTotal Investment: " + str(total))

print("\nPortfolio saved successfully in portfolio.txt")