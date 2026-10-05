def summing_number(score):
    return sum(score)

def average_counting(total,subject=5):
    return total/subject

def result(student,score,):
    sum = summing_number(score)
    average = average_counting(sum)
    print(student)
    print(f"scores: {sum}")
    print(f"average: {average}")
result("joseph", [12,45,56,7,43,5,4])
