import numpy as np

class Employee:

  num_of_employee = 0     # class variable use to counts employees
  raise_amount = 1.04     # class variable use to raise basicpay

  def __init__(self, firstName, lastName, age, email, desig, basicpay):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.desig = desig
    self.basicpay = basicpay
    self.idNo = np.random.randint(1,1000,1)

    if self.idNo % 2 == 0:         # if generated number is even then subtract it by 10
      self.idNo = self.idNo - 10

    else:
      self.idNo = self.idNo + 10   # if generated number is odd then add 10 in it
    
    self.idNo = abs(self.idNo)

    print(f"\n{self.idNo} ID number is assigned to {self.firstName +' '+ self.lastName}\n")

    Employee.num_of_employee += 1      # increment each time when new employee added

 
  def displayAll(self):
      print(f"\nFull name of Employee is : {self.firstName+' '+self.lastName}")
      print(f"Age of Employee is : {self.age}")
      print(f"ID of Employee is : {self.idNo}")
      print(f"Desig of Employee is : {self.desig}")
      print(f"Basic pay of Employee is : {self.basicpay}")

  def updateDesig(self,desig):
    self.desig = desig

  def displayName(self):
    return self.firstName+' '+self.lastName

  def displayAge(self):
    return self.age

  def displayPay(self):
    return self.basicpay
  
  def apply_raise(self):
    self.basicpay = float(self.basicpay * self.raise_amount)

  # @classmethod
  # def set_raise_amount(cls,new_amount):
  #   cls.raise_amount = new_amount

# def menu():
#   print('\n       ------------------- Employee Record Management System -------------------       \n')
#   print("Enter 1 to ADD new Record")
#   print("Enter 2 to Display all new Records")
#   print("Enter 3 to Display specific Record")
#   print("Enter 4 to update existing Record")
#   print("Enter 0 to exit program\n")
#   choice = input("Enter your choice: ")

#   return choice

if __name__ == '__main__':

    print('\n       ------------------- Employee Record Management System -------------------       \n')
    fname = input("Enter first name of Employee: ")
    lname = input("Enter last name of Employee: ")
    age = input("Enter age of Employee: ")
    desig = input("Enter desig of Employee: ")
    email = input("Enter email of Employee: ")
    basicpay = float(input("Enter basic pay of Employee: "))

    
    emp_1 = Employee(fname,lname,age,email,desig,basicpay)
    
    disp_choice = input("\nDo you want to display data of Employee (Y/N)")

    if disp_choice.lower() == 'y':
      fname, lname, age, id, desig, basicpay = emp_1.displayAll()

      print(f"\nFull name of Employee is : {fname+''+lname}")
      print(f"Age of Employee is : {age}")
      print(f"ID of Employee is : {id}")
      print(f"Desig of Employee is : {desig}")
      print(f"Basic pay of Employee is : {basicpay}")

test_user = Employee("Test","User",20,'abc@example.com','datascientist',3444)

test_user.displayAll()

test_user.updateDesig("Data Science Manager")

test_user.displayAll()

print(test_user.displayPay())

print(test_user.apply_raise())

print(test_user.displayPay())

print(Employee.num_of_employee)

