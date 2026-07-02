from bot.orders import market_buy

symbol = input("Enter symbol (example BTCUSDT): ").upper()
qty = float(input("Enter quantity: "))

try:
    order = market_buy(symbol, qty)
    print("\nOrder placed successfully!\n")
    print(order)
except Exception as e:
    print("\nError:", e)