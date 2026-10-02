# ============================================
# Stock Portfolio Tracker
# CodeAlpha Internship Project
# ============================================

import csv


# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}


# Display available stocks
def display_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock:<10} ${price}")

    print("-" * 30)


# Create user's portfolio
def create_portfolio():
    portfolio = []

    while True:
        try:
            count = int(input("\nHow many stocks do you want to add? "))

            if count <= 0:
                print("Please enter a number greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    for i in range(count):

        while True:
            stock = input(
                f"\nEnter stock symbol {i + 1}: "
            ).upper()

            if stock in stock_prices:
                break
            else:
                print(
                    "Invalid stock symbol. "
                    "Please choose from the available stocks."
                )

        while True:
            try:
                quantity = int(
                    input(f"Enter quantity of {stock}: ")
                )

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Please enter a valid quantity.")

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append({
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "investment": investment
        })

    return portfolio


# Calculate total investment
def calculate_total(portfolio):
    total = 0

    for item in portfolio:
        total += item["investment"]

    return total


# Display portfolio summary
def display_portfolio(portfolio):

    print("\n" + "=" * 60)
    print("                PORTFOLIO SUMMARY")
    print("=" * 60)

    print(
        f"{'Stock':<10}"
        f"{'Price':<12}"
        f"{'Quantity':<12}"
        f"{'Investment':<15}"
    )

    print("-" * 60)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"${item['price']:<11}"
            f"{item['quantity']:<12}"
            f"${item['investment']:<15}"
        )

    print("-" * 60)

    total = calculate_total(portfolio)

    print(f"{'TOTAL INVESTMENT':<34} ${total}")
    print("=" * 60)


# Save portfolio to CSV
def save_portfolio(portfolio):

    filename = "portfolio.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Stock",
            "Price",
            "Quantity",
            "Investment"
        ])

        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["price"],
                item["quantity"],
                item["investment"]
            ])

        total = calculate_total(portfolio)

        writer.writerow([])
        writer.writerow([
            "Total Investment",
            total
        ])

    print(
        f"\nPortfolio saved successfully to {filename}"
    )


# Main program
def main():

    print("=" * 50)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    display_stocks()

    portfolio = create_portfolio()

    display_portfolio(portfolio)

    save_portfolio(portfolio)


# Program entry point
if __name__ == "__main__":
    main()