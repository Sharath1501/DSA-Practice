class emplyee:
    def addemplyee(self):
        self.empid = input("Enter the employee id: ")
        self.empname = input("nter employee name: ")
        self.empdesig = input("ENter employee designation")
        self.empexperience = int(input("Enter employee experience:"))
        self.empage = int(input("Enter age of employee: "))
    def display(self):
        print(f"Employee id :{self.empid}")
        print(f"Employee name : {self.empname}")
        print(f"Employee designation:{self.empdesig}")
        print(f"Employee experience:{self.empexperience}")
        print(f"Employee age:{self.empage}")
    def calculate(self,basic):
        if self.empage<30 and self.empexperience>5:
            final_salary = 0.5*basic
        elif self.empage < 40 and self.empexperience > 5:
            final_salary = 1.75 * basic
        elif self.empage < 40 and self.empexperience > 10:
            final_salary = 2 * basic
        elif self.empage < 50 and self.empexperience > 20:
            final_salary = 2.25 * basic
        elif self.empage < 50 and self.empexperience > 25:
            final_salary = 2.5 * basic
        elif self.empage < 58 and self.empexperience > 30:
            final_salary = 3 * basic
        else:
            final_salary = basic
        print(f"calcaulated salary:{final_salary:.2f}")

emp = emplyee()
emp.addemplyee()
emp.display()
emp.calculate(20000)