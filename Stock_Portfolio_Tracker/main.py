import json
import os

DATA_FILE = "portfolio.json"


# Load portfolio from JSON file
def load_portfolio():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            print("Error loading portfolio. Starting empty.")

    return []


# Save portfolio to JSON file
def save_portfolio(portfolio):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(portfolio, file, indent=4)

        print("Portfolio saved successfully!")

    except OSError as error:
        print("Error saving portfolio:", error)


# Get a positive number
def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Enter a valid number.")


# Add a stock
def add_stock(portfolio):
    print("\n--- Add New Stock ---")

    company = input("Enter company name: ").strip()
    symbol = input("Enter stock symbol: ").strip().upper()

    if not company or not symbol:
        print("Company name and symbol cannot be empty.")
        return

    for stock in portfolio:
        if stock["symbol"] == symbol:
            print("This stock already exists.")
            return

    quantity = get_positive_number("Enter quantity: ")
    purchase_price = get_positive_number("Enter purchase price: ")

    stock = {
        "company": company,
        "symbol": symbol,
        "quantity": quantity,
        "purchase_price": purchase_price,
        "current_price": purchase_price
    }

    portfolio.append(stock)
    save_portfolio(portfolio)

    print(f"{company} added successfully!")


# View portfolio
def view_portfolio(portfolio):
    print("\n--- Your Stock Portfolio ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    for stock in portfolio:
        investment = stock["quantity"] * stock["purchase_price"]
        current_value = stock["quantity"] * stock["current_price"]

        profit_loss = current_value - investment
        percentage = (profit_loss / investment) * 100

        print("-" * 40)
        print("Company:", stock["company"])
        print("Symbol:", stock["symbol"])
        print("Quantity:", stock["quantity"])
        print("Purchase Price:", stock["purchase_price"])
        print("Current Price:", stock["current_price"])
        print("Total Investment:", round(investment, 2))
        print("Current Value:", round(current_value, 2))
        print("Profit/Loss:", round(profit_loss, 2))
        print("Profit/Loss Percentage:", round(percentage, 2), "%")

    print("-" * 40)


# Calculate total investment
def calculate_investment(portfolio):
    total = sum(
        stock["quantity"] * stock["purchase_price"]
        for stock in portfolio
    )

    print(f"\nTotal Investment: Rs. {total:.2f}")


# Update stock price
def update_stock_price(portfolio):
    symbol = input("\nEnter stock symbol to update: ").strip().upper()

    for stock in portfolio:
        if stock["symbol"] == symbol:
            new_price = get_positive_number("Enter new current price: ")

            stock["current_price"] = new_price
            save_portfolio(portfolio)

            print("Stock price updated successfully!")
            return

    print("Stock not found!")


# Calculate overall profit/loss
def calculate_profit_loss(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    total_investment = 0
    total_current_value = 0

    for stock in portfolio:
        investment = stock["quantity"] * stock["purchase_price"]
        current_value = stock["quantity"] * stock["current_price"]

        total_investment += investment
        total_current_value += current_value

    profit_loss = total_current_value - total_investment
    percentage = (profit_loss / total_investment) * 100

    print("\n--- Portfolio Summary ---")
    print(f"Total Investment: Rs. {total_investment:.2f}")
    print(f"Current Portfolio Value: Rs. {total_current_value:.2f}")
    print(f"Overall Profit/Loss: Rs. {profit_loss:.2f}")
    print(f"Profit/Loss Percentage: {percentage:.2f}%")

    if profit_loss > 0:
        print("Status: You are in PROFIT!")
    elif profit_loss < 0:
        print("Status: You are in LOSS!")
    else:
        print("Status: No Profit, No Loss.")


# Remove a stock
def remove_stock(portfolio):
    symbol = input("\nEnter stock symbol to remove: ").strip().upper()

    for stock in portfolio:
        if stock["symbol"] == symbol:
            portfolio.remove(stock)
            save_portfolio(portfolio)

            print("Stock removed successfully!")
            return

    print("Stock not found!")


# Main application
def main():
    portfolio = load_portfolio()

    while True:
        print("\n" + "=" * 40)
        print("       STOCK PORTFOLIO TRACKER")
        print("=" * 40)

        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Calculate Total Investment")
        print("4. Update Current Stock Price")
        print("5. Calculate Overall Profit/Loss")
        print("6. Remove Stock")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            view_portfolio(portfolio)

        elif choice == "3":
            calculate_investment(portfolio)

        elif choice == "4":
            update_stock_price(portfolio)

        elif choice == "5":
            calculate_profit_loss(portfolio)

        elif choice == "6":
            remove_stock(portfolio)

        elif choice == "7":
            save_portfolio(portfolio)
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Select between 1 and 7.")


if __name__ == "__main__":
    main()