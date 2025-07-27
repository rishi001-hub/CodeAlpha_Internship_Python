import csv

# Hardcoded dictionary of stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180.00,    # Apple
    "TSLA": 250.00,    # Tesla
    "GOOGL": 2750.00,  # Alphabet
    "MSFT": 310.00,    # Microsoft
    "AMZN": 3300.00,   # Amazon
    "NFLX": 550.00,    # Netflix
    "META": 350.00     # Meta (Facebook)
}
def get_user_input():
    """
    Collects stock name and quantity from user.
    Returns a dictionary of stock symbols and quantities.
    """
    print("\n📈 Welcome to the Stock Portfolio Tracker!")
    print("Enter stock symbols and quantity owned.")
    print("Type 'done' when finished.\n")

    portfolio = {}
    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        if stock == 'DONE':
            break
        if stock not in STOCK_PRICES:
            print("⚠️ Stock not in our price list. Please try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("❌ Quantity cannot be negative. Try again.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
    return portfolio

def calculate_investment(portfolio):
    """
    Calculates total investment based on stock prices and quantities.
    """
    total = 0.0
    print("\n📊 Investment Summary:")
    print("-" * 30)
    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * quantity
        total += investment
        print(f"{stock:<6} | Quantity: {quantity:<4} | Price: ${price:<8} | Value: ${investment:.2f}")
    print("-" * 30)
    print(f"💰 Total Investment: ${total:.2f}")
    return total

def save_to_file(portfolio, total):
    """
    Saves investment details to a .txt or .csv file based on user choice.
    """
    choice = input("\nDo you want to save this report? (yes/no): ").strip().lower()
    if choice not in ('yes', 'y'):
        print("Report not saved.")
        return

    file_type = input("Save as (1) TXT or (2) CSV? Enter 1 or 2: ").strip()
    
    if file_type == '1':
        with open("investment_report.txt", "w") as file:
            file.write("Stock Portfolio Report\n")
            file.write("----------------------------\n")
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                file.write(f"{stock} - Quantity: {quantity}, Price: ${price}, Value: ${value:.2f}\n")
            file.write("----------------------------\n")
            file.write(f"Total Investment: ${total:.2f}\n")
        print("📁 Report saved as investment_report.txt")

    elif file_type == '2':
        with open("investment_report.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                writer.writerow([stock, quantity, price, f"{value:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", f"${total:.2f}"])
        print("📁 Report saved as investment_report.csv")
    
    else:
        print("❌ Invalid choice. File not saved.")

def main():
    portfolio = get_user_input()
    if not portfolio:
        print("No stocks entered. Exiting...")
        return
    total = calculate_investment(portfolio)
    save_to_file(portfolio, total)

# Run the tracker
if __name__ == "__main__":
    main()
