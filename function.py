def sumtotal(price):
    return sum(price)

def tip_didcuction(amount, tips=0.15):
    return amount * tips

def per_person(total, person):
    return total / person


def print_recietpt(cutomer, price, person):
    adding_up = sumtotal(price)
    our_tip = tip_didcuction(adding_up)
    final = adding_up + our_tip
    split = per_person(final , person)
    print(f"{cutomer}")
    print(f"list of price: {adding_up:.2f}")
    print(f"tip: {our_tip:.2f}")
    print(f"total: {final:.2f}")
    print(f"per person :{split:.2f}")
print_recietpt("joosph", [200,2300,500, 7000], 5)    