from pathlib import Path
import json
JSON_FILE = Path(__file__).resolve().parent / "work_flow.json"

ticket_count = 1
tickets = []
def load_ticket():
    if not JSON_FILE.exists():
        return []
    try:
        with open(JSON_FILE, "r")as file:
           return json.load(file)
    except json.JSONDecodeError:
            return [] 

def save_ticket(ticket):
    tickets = load_ticket()
    tickets.append(ticket)    

    with open(JSON_FILE, "w") as file:
        json.dump(tickets,file, indent=2)       

def create_ticket():
    global ticket_count

    ticket_id = f"T{str(ticket_count).zfill(3)}"
    ticket_count += 1
    
    while True:
        student_name = input("what is you name? ".strip())
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
                raise ValueError(f"\t{"="*5} discription must no be empty try again {"="*5}\n").upper()
        except (ValueError)as error:
            print(error)
            continue
        
        try:
            problem_discription = int(problem_discription)
            if problem_discription < 1:
                raise ValueError("choose from 1,2,3,4,5")
            if problem_discription > 5:
                raise ValueError("choose from 1,2,3,4,5")
        except (ValueError) as mumu:
                print(mumu)
                continue   
        if problem_discription  == 1:
            problem_discription = "wifi is down"
            print(problem_discription)

        elif problem_discription == 2:
            problem_discription = "student cannot access the school portal"
            print(problem_discription)

        elif problem_discription == 3:
            problem_discription = "electricity issues"
            print(problem_discription)

        elif problem_discription == 4:
            problem_discription = "bank issues"
            print(problem_discription) 

        elif problem_discription == 5:
            while True:
                problem_discription =input("write in detail what is the issue? ").strip()
                
                try: 
                    if problem_discription.isdigit():
                      raise ValueError("it must write in detail")
                  
                except (ValueError)as file:
                    print(file)
                    continue
                print(problem_discription)
                break
        else:
            print("invalid input try again")
            continue                    
        break
    while True: 
        affected_users = input("How ,many users are affected? ".strip())
        try:
            if affected_users == "":
                 raise ValueError("the must be an affected user")
            
            affected_users = int(affected_users)
            if affected_users < 1:
                raise ValueError("at least one user must be affected and must be a positive number ")
        except (ValueError) as pig:
            print(f"{pig} it must be an whole number")
            continue
        print(affected_users)     
        break
    while True:
            print("\nlist of urgencys".upper())
            print("1. High")
            print("2. Medium")
            print("3. Low")
            urgency =  (input("\nwhat is the urgency choose from 1,2,3").strip())
            try:
                urgency = int(urgency)
                if not urgency:
                    raise ValueError("urgency most not be empty")
              
                if urgency < 1:
                    raise ValueError("choose from 1,2,3 option")
                if urgency > 3:
                    raise ValueError("choose from 1,2,3 option")
            except (ValueError) as bugi:
                print(bugi)
                continue
            if urgency == 1:
                urgency = "High"
            elif urgency == 2:
                urgency = "Medium"
            elif urgency == 3:
                urgency = "Low"
            else:
                print("invalid input choose from 1-3 option") 
                continue
            break
         
    if urgency == "High" and  affected_users > 10:
        priority = "critical"
        print(priority)

    elif urgency == "High" or affected_users >= 10:
        priority = "high"
        print(priority)

    elif urgency == "Medium" or affected_users >= 5:
        priority = "medium"  
        print(priority)  

    else:
        priority = "low" 
        print(priority)  

    ticket = {
              "ticket_id": ticket_id,
              "name": student_name,
              "problem": problem_discription,
              "urgency": urgency,
              "affected useer": affected_users,
              "priority": priority
              }
    tickets.append(ticket)
    print(tickets)

    
    return student_name,problem_discription,urgency,affected_users,priority,ticket_id
create_ticket()

