class Employee:
    def __init__(self, name, base_salary, bonus_hrs, sales):
        self.name = name
        self.base_salary = base_salary
        self.bonus_hrs = bonus_hrs
        self.sales = sales

    def calculate_net_salary(self):
        bonus = self.bonus_hrs * 10 
        return self.base_salary + bonus + (self.sales * 0.05)

    def info(self):
        net_salary = self.calculate_net_salary()
        print(f'The employee {self.name} has a base salary of {self.base_salary} DHS, sales of {self.sales}, and a net salary of {net_salary} DHs')


emp1 = Employee("Skerteh", 10000, 30, 500)
emp1.info()