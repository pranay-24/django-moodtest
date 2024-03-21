# def myfunc(name, *args , **kwargs):
#     print(name,args, kwargs)

from dataclasses import dataclass
from typing import List
@dataclass
class Employee:
    role: str
    name: str
    vacationdays: int = 25
    
    
    def take_payout(self):
        payout = 0
        
        if self.vacationdays >= 5:
            self.vacationdays -=5
            payout = 100 * 5
        return payout , self.vacationdays


class Company:
    
    def __init__(self):
        self.employees : List[Employee]= []
        
    def add_employee(self , employee:Employee):
             self.employees.append(employee)
    def find_managers (self) -> List[Employee]:
             managers = []
             for employee in self.employees:
                 if employee.role =='manager':
                     managers.append(employee) 
             return managers  

    def find_interns (self) -> List[Employee]:
             interns = []
             for employee in self.employees:
                 if employee.role == 'intern':
                     interns.append(employee) 
             return interns  
         
def main() -> None:
    john = Employee(role="Manager", name="John")
    payout, remaining = john.take_payout()
    payout2 = john.take_payout()
    print(payout, remaining)
    
if __name__ == "__main__":
    main()