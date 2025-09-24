# Converts between a few popular currencies using fixed rates.

print(" Welcome to the Simple Currency Converter!\n")

# Fixed exchange rates (as an example)
exchange_rates = {
    "USD": 1.0,        # Base currency
    "EUR": 0.91,
    "GBP": 0.78,
    "PKR": 280.0,
    "JPY": 150.0
}

print("Supported currencies:", ", ".join(exchange_rates.keys()))

try:
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("From (currency code, e.g., USD): ").upper()
    to_currency = input("To (currency code, e.g., EUR): ").upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Sorry, one of the currencies is not supported.")
    else:
        # Convert amount to USD first, then to target currency
        amount_in_usd = amount / exchange_rates[from_currency]
        converted_amount = amount_in_usd * exchange_rates[to_currency]
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

except ValueError:
    print("Invalid amount! Please enter a number.")
