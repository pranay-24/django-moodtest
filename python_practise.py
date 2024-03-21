# def myfunc(name, *args , **kwargs):
#     print(name,args, kwargs)

from dataclasses import dataclass

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


def main() -> None:
    john = Employee(role="Manager", name="John")
    payout, remaining = john.take_payout()
    payout2 = john.take_payout()
    print(payout, remaining)
    
if __name__ == "__main__":
    main()