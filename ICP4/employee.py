class employee:
    """A class representing employee"""
    salary_count = 0  #initializing salary_count
    employee_count=0 #initializing employee_count
    def __init__(self,name,family,salary,dept):
        self.name= name #declaring name
        self.family=family #declaring family
        self.salary=salary #declaring salary
        self.dept=dept #declaring department
#adding the employee and salary count every time a new employee is called
        employee.employee_count +=1
        employee.salary_count += salary
#return the attributes
#returning name
    def get_name(self):
        return self.name
#returning family
    def get_family(self):
        return self.family

    def get_dept(self):
        return self.dept

    def get_salary(self):
        return self.salary
#function for averaging the salary
    def average_salary():
        print ("average salary is:", employee.salary_count/employee.employee_count)
    def employee_number():
        print ("employee number is:", employee.employee_count)
        
#inheritance of the previous class
class fulltime_employee(employee):
    """A class representing fulltime employee"""    
    def __init__(self,name,family,salary,dept,time):
        employee.__init__(self,name,family,salary,dept) #Call __init__ for employee
        self.time = time
    def get_job_des(self):
        print (self.time)
  
a = employee("Bob", "A", 25000,"acc")
b = employee("farid","S",30000,"eng")
c = fulltime_employee("Ahmed","Z",50000,"eng","Full_time")
d = fulltime_employee("Zarin","F",50000,"eng","Full_time")
