def create_ticket():
    
    while True:
        student_name = input("what is you name? ")
        try:
           
            if student_name == "":
                raise ValueError("Name should not be empty")   
        except ValueError as monkey:
            print(monkey)   
            continue
        print(student_name)
        break
        
    while True:  
        print("\nlist of problems avalible".upper())
        print("1. wifi is down")
        print("2. student can access the school portal")
        print("3. electricity issues")
        print("4. bank issues")
        print("5. others")
        problem_discription =  (input("what are the  problem you are facing ").strip())
        try:
            if problem_discription == "":
                raise ValueError(f"\t{"="*5} discription must no be empty try again {"="*5}\n".upper())
        except (ValueError)as error:
            print(error)
            continue
        
        try:
            problem_discription = int(problem_discription)
            if not isinstance(problem_discription, int):
                raise ValueError("it must be a whole number from (1-5)")
        except (ValueError) as mumu:
                print(mumu)
                continue    

        if problem_discription  == 1:
            problem = "wifi is down"
            print(problem)

        elif problem_discription == 2:
            problem = "student can access the school portal"
            print(problem)

        elif problem_discription == 3:
            problem = "electricity issues"
            print(problem)

        elif problem_discription == 4:
            problem = "bank issues"
            print(problem) 

        elif problem_discription == 5:
            while True:
                if problem == "":
                    raise ValueError("they must be a issue note")
                problem = int(input("write in detail what is the issue? ")).strip()
                problem = str(problem)
                try: 
                    if not isinstance(problem, str):  
                      raise ValueError("it must write in detail")
                    if not problem:
                        raise ValueError("the must be a problem")
                except (ValueError)as file:
                    print(file)
                    continue
                print(problem)
                break      
        else:
            print("invalid input try again")
            continue                 
        break
    return student_name,problem_discription
           
        
        
            

           
        
    
    
def input_validation(urgency,affected_users):

    if isinstance(affected_users, (float, bool)):
            raise ValueError("affected user must be a whole number")
    
    try:
        affected_users = int(affected_users)
    except ValueError:
        raise ValueError("invalid input, it must be an number not other words")   

    if urgency not in ["high", "medium", "low"]:
        raise ValueError("invalid input choos from (high medium low)")        
    
    if affected_users < 1:
        raise ValueError("at least one user must be affected and must be a positive number ")

    if not isinstance(affected_users, int):
        raise ValueError("invalid input, it must be an number not other words")
    return affected_users,urgency


def calculate_priority(urgency, affected_users,priority):

    if urgency == "high" and  affected_users >= 10:
        priority = "critical"

    elif urgency == "high" or affected_users >= 10:
        priority = "high"

    elif urgency == "meduim" or affected_users >= 5:
        priority = "meduim"    

    elif urgency == "low"  or affected_users >=1: 
        priority = "low"   
    return priority
create_ticket()  