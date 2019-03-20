class Employee:
    def __init__(self, name, identity, employee_type):
        self.name =name
        self.identity = identity
        self.employee_type = employee_type

class WorkerClass(Employee):
    def __init__(self, name, identity, employee_type, shift, rate):
        super().__init__(name, identity, employee_type)
        self.shift = ''
        self.rate = ''
    def __str__(self):
        return 'W- '+'Name: '+str(self.name)+' '+'ID: '+str(self.identity)+' '+'Shift: '+str(self.shift)+' '+'Rate: '+str(self.rate)
class SupervisorClass(Employee):
    def __init__(self, name, identity, employee_type, salary, bonus):
        super().__init__(name, identity, employee_type)
        self.salary = ''
        self.bonus = ''
    def __str__(self):
        return 'S- '+'Name: '+str(self.name)+' '+'ID: '+str(self.identity)+' '+'Salary: '+str(self.salary)+' '+'Bonus: '+str(self.bonus)