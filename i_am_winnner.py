def smallest_number(numbers):
    smallest = numbers[0]
    for b in numbers:
        if b < smallest:
            smallest = b
    return f"{smallest} is the smallest number"

def highest_number(number):
    highest = number[0]
    for b in number:
        if b > highest:
            highest= b
    return f"{highest}  is the highest number in the list"
        
print(smallest_number([2,5,3,9,6,15,4,0,7,10]))
