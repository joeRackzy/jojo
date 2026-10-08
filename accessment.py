def highest_number(numbers):
    first = numbers[0]
    for n in numbers:
        if n > first:
            first= n
    return(first)
print(highest_number([2,34,4,54,67,67,676,67,1,76]))

def price_text(price1):
    return int(price1)

def discount(amount,discount= 0.10):
    return amount * discount

def finall(customer, price1,):
    summing = price_text(price1)
    summing1 = summing *2
    discounting = (discount(summing1))
    total = summing1 - discounting


    print(customer)
    print(summing)
    print(summing1)
    print(discounting)
    print(total)
finall("joseph", "3000")

def together(price, amount):
    total = int(price)*amount
    print(total)
totallly = together("7",5)
print(totallly)