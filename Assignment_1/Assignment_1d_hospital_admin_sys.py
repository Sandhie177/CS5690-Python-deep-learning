#Write a python program to create the a Hospital admission System 
class Person(object): #1ST CLASS
    #for defining sex
    sex = ('male', 'female', 'others')
    #defining constructor
    def __init__(self,name,age,sex): #USE OF INIT CONSTRUCTOR
       #defining name attribute 
      
        self.__name = name #PRIVATE ATTRIBUTE
        #defining age attribute
        self.age = age #SELF USE
        #defining sex attribute
        if sex == 'M':
            self.sex = Person.sex[0]
        elif sex == 'F':
            self.sex = Person.sex[1]
        else:
            self.sex = Person.sex[2]
    #function to get all the descriptions 
    def getdescription(self):
        return self.__name + '\t' + str(self.age) + '\t' + self.sex
     #function to get name       
    def getname(self):
        return self.__name
	#function to get age
    def getage(self):
        return self.age
    #function to get sex
    def getsex(self):
        return self.sex   
#creating 2nd class patient with the inheritance of person    
class Patient(Person): #2ND CLASS
    pass #to get the name of class
    #defining constructor
    def __init__(self,name,age,sex,status,illness, insurance_name, policy_id):
        #inheriting attributes from person class
        Person.__init__(self,name,age,sex)
        #defining attributes
        self.status = status
        self.illness = illness
        self.insurance_name = insurance_name
        self.policy_id = policy_id
      #defining functions for getting attributes  
    def getstatus(self):
        return self.status
    
    def getillness(self):
        return self.illness
    
    def getinsurance_name(self):
        return self.insurance_name
    
    def getpolicy_id(self):
        return self.policy_id
#creating 3rd class patient with the inheritance of person        
class Doctor(): #3RD CLASS
    pass #to get the name of class
    #defining constructor
    def __init__(self,doc_name,doc_age,expertise):
        #defining attributes
        #defining name attribute 
        self.doc_name = doc_name 
        #defining age attribute
        self.doc_age = doc_age #SELF USE
        self.expertise = expertise
        
    #defining functions for getting attributes    
    #function to get name       
    def getdoc_name(self):
        return self.doc_name
	#function to get age
    def getdoc_age(self):
        return self.age
    def getexpertise(self):
        return self.expertise
#creating 4th class patient with the inheritance of person     
class Nurse(Person): #4TH CLASS
    pass #to get the name of class
    #defining constructor
    def __init__(self,name,age,sex,department):
        #inheriting attributes from person class
        super(Nurse,self).__init__(name,age,sex)
        #defining attributes
        self.department = department
     #defining functions for getting attributes   
    def getdepartment(self):
        return self.department
  #creating 5th class patient with the inheritance of person      
class Clerk(Person): #5TH CLASS
    pass #to get the name of class
    #defining constructor
    def __init__(self,name,age,sex,department):
        #inheriting attributes from person class
        Person.__init__(self,name,age,sex)
        #defining attributes
        self.department = department
     #defining functions for getting attributes   
    def getdepartment(self):
        return self.department    
#creating 6th class patient with the inheritance of Patient 
     
class Book(Patient,Doctor):    #MULTIPLE INHERITANCE
    pass #to get the name of class by the command e.__class__.__name__
      #defining constructor
    def __init__(self,name,age,sex,status,illness,insurance_name, policy_id,doc_name,doc_age,expertise,time,date):
       #inheriting attributes from patient class 

        Patient.__init__(self,name,age,sex,status,illness,insurance_name, policy_id)
        Doctor.__init__(self,doc_name,doc_age,expertise)
        self.time = time
        self.date = date
 #defining functions for getting attributes       
      
    def gettime(self):
        return self.time
    
    def getdate(self):
        return self.date
a= Patient ("Bob",50,"M", "married","Heart","atenna",1234)
b= Doctor ("Martina",30,"Surgery")
c= Nurse ("Daphane",25,"F","cardio")
d= Clerk ("Micky",40,"M","Administration")
e= Book("farid",27,'M','married','Burn','Atena',1234,'Martina','30',"Surgery",'3pm','09/12/2018')
        

   
    
    
    
    
    
    
    