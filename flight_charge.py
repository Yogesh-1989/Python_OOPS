def flight_charges(price):
  uppgrade = input("Would you like to upgrade.?").lower()
  if uppgrade=="yes":
    price+=99
  baggage = input("Will you have a baggage.?").lower()
  if baggage=="yes":
    price +=35
  tax =(price * 0.08) + price
  return tax

price = int(input("Enter a base fare: "))

grand_total = flight_charges(price)
print("Grand total after tax", grand_total)