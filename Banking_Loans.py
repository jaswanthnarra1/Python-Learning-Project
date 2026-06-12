import os
from datetime import datetime
import json

file = "loans.json"
Min_salary = 20000

def load_data():
    if not os.path.exists(file):
        return []
    with open(file,'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def safe_date_input(msg):
     while True:
         date_str = input(msg)

         try:
             datetime.strptime(date_str,"%d-%m-%Y")
             return date_str
         except ValueError:
             print("Enter valid date")

def next_due(start_date):
    d = datetime.strptime(start_date,"%d-%m-%Y")

    if d.month == 12:
        nxt = d.replace(year=d.year + 1,month=1)
    else:
        nxt = d.replace(month=d.month+1)
    return nxt.strftime("%d-%m-%Y")

def generate_id(data):
    if not data:
        return 1001
    
    max_id = max(['loan_id'] for loan in data)
    return max_id + 1

def save_data(data):
    with open(file,'w') as f:
        json.dump(data,f,indent=2)

def find_loan(data,loan_id):
    for loan in data:
        if loan['loan_id'] == loan_id:
            return loan
    return None
         
        
def apply_loan(data):
    name = input("Enter Full name: ")
    try:
        salary = int(input("Enter Your Monthly Salary: "))
    except ValueError:
        print("Not Valid Amount")
        return
    
    if salary <= Min_salary:
        print(f'Salary must be more than {Min_salary} to get a loan')
        return
    
    loan_amt = salary * 10
    emi = int(salary * 0.10)
    months = loan_amt // emi

    print(f'Congratulations!! {name} :) Youre Eligible ')
    print(f'Loan Amount: {loan_amt}')
    print(f'EMI: {emi}')
    print(f'Current Tenure: {months}')

    confirm = input("Do you want to Proceed(Yes/No): ".lower())
    if confirm != 'yes':
        print('Loan Cancelled\n')
    
    start_date = safe_date_input("Enter Loan Start Date(dd-mm-yyyy): ")
         
    first_due = next_due(start_date)

    loan_id = generate_id(data)

    record = {
        "loan_id":loan_id,
        "name": name,
        "salary": salary,
        "loan_amount": loan_amt,
        "emi": emi,
        "tenure": months,
        "balance" : loan_amt,
        "status": "On Going",
        "next_due": first_due,
        "history":[]
    }

    data.append(record)
    save_data(data)
    print(f'Loan Approved. Your loan id: {loan_id}')

def pay_emi(data):
       try:
           load_id = int(input("Enter your loan id: "))
       except ValueError:
           print('Invalid loan ID.\n')
           return
       
       loan = find_loan(data,loan_id=0)
       if not loan:
           print('Loan not founf!\n')
           return
       if loan['status'] == "CLeared":
           print("Loan Cleared")
           return
       print(f'Next emi due {loan['next_due']}')

       try:
           amt = int(input(f'Enter EMI ({loan['emi']})'))
       except ValueError:
           print("Invalid amount.\n")   

       if amt != loan['emi']:
           print(f'Wrong Emi Amount,Expected({loan['emi']}),got(amt)')
           return
        
       loan["balance"] -= amt
       loan["tenure"] -= 1
       loan['history'].append({"date":loan["next_due"],"amount":amt})
       loan['next_due'] = next_due(loan["next_due"])

       if loan['balance'] <= 0:
           loan['status'] = "Cleared"
           loan['balace'] = 0
           loan['tenure'] = 0
           print("Loan Cleared")
       else:
           print(f'Emi paid,, balance left:{loan[balance]}\n Remaning Tenure: {loan['tenure']}month')
       save_data(data)
      

       
def main():

    data = load_data()
    print(data)

    while True:
        print("=========================")
        print("===  Bank Loan System ===")
        print("=========================")
        print("1. Apply Loan")
        print("2. Pay EMI")
        print("3. Clear Loan")
        print("4. View Payment History")
        print("5. Exit")
        
        choice = input("Enter Your Choice: ")

        if choice == "1":
            apply_loan(data)
        elif choice == "2":
            pay_emi(data)
        elif choice == "3":
            clear_loan(data)
        elif choice == "4":
            view_history(data)
        elif choice == "5":
            print("Thanks For Reaching:)")
            break
        else:
            print("Invalid Entry Please Reconnect Again")

main()

