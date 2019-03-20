from w11_EmployClass import Employee
from w11_EmployClass import WorkerClass
from w11_EmployClass import SupervisorClass

emp_dict = {}

def addEmp():
    emp = Employee(' ', 0, 0)
    emp.identity = int(input('Please enter the employee ID : '))
    emp.name = str(input('The employee name : '))
    emp.employee_type = int(input('Type (1) Woker (2) Supervisor : '))
        
    if emp.employee_type == 1:
        shift_c = 0
        wk = WorkerClass(emp.name, emp.identity, emp.employee_type, ' ', 0)
        shift_c = int(input('Shift (1) day (2) night : '))
        if shift_c == 1:
            wk.shift = '日班'
        elif shift_c == 2:
            wk.shift = '夜班'
        wk.rate = int(input('Rate : '))
    
        if emp.identity not in emp_dict:
            emp_dict[emp.identity] = wk
            print('The endtry has been added\n')
        else:
            print('The employee ID exist.\n')
    elif emp.employee_type == 2 :
        sp = SupervisorClass(emp.name, emp.identity, emp.employee_type, 0, 0)
        sp.salary = int(input('Salary : '))
        sp.bonus = int(input('Bonus : '))
            
        if emp.identity not in emp_dict:
            emp_dict[emp.identity] = sp
            print('The endtry has been added\n')
        else:
            print('The employee ID exist.\n')
    
def listAll():
    for key in emp_dict:
        print(emp_dict[key])

def main():
    print("--------- Menu ---------\n1. Add a new employee\n2. List all\n0. Quit the program/nEnter your choice:")
    choose = int(input("Enter your choice: "))
    while True:
        if choose == 1:
            addEmp()
            print("--------- Menu ---------\n1. Add a new employee\n2. List all\n0. Quit the program/nEnter your choice:")
            choose = int(input("Enter your choice: "))
        elif choose == 2:
            listAll()
            print("--------- Menu ---------\n1. Add a new employee\n2. List all\n0. Quit the program/nEnter your choice:")
            choose = int(input("Enter your choice: "))
        elif choose == 0:
            exit()
main()
