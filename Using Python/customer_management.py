import numpy as np

class Person():       # super class
  def __init__(self,fname,lname,age,country,email):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.country = country
    self.email = email

# ------------------------------------------------------------

class Customer(Person):   # subclass of Person
  total_customer = 0
  def __init__(self,fname,lname,country,email,address,age,product,wishlist=None):
    super().__init__(fname,lname,age,country,email)
  
    self.address = address
    # self.age = age
    self.product = product    
    self.wishlist = []

    self.idNo = np.random.randint(1,1000,1)

    if self.idNo % 2 == 0:         # if generated number is even then subtract it by 10
      self.idNo = self.idNo - 10
    else:
      self.idNo = self.idNo + 10   # if generated number is odd then add 10 in it

    self.idNo = abs(self.idNo)

    print(f"\n{self.idNo} ID number is assigned to {self.fullName()}\n")

    Customer.total_customer += 1

  def fullName(self):
    return self.fname+" "+self.lname

  def getEmail(self):
    return self.email
  
  def getCountry(self):
    return self.country
  
  def getProduct(self):
    return self.product
  
  def getAge(self):
    return self.age

  def displayDetails(self):
    print("\n------------------ Customer Detail ------------------ ")
    print(f"Full name of Customer is: {self.fullName()}")
    print(f"Customer's country is: {self.getCountry()}")
    print(f"Email of {self.fullName()} is: {self.getEmail()}")
    print(f"Age of {self.fullName()} is: {self.getAge()}")
    print(f"Customer wants to purchase: {self.getProduct()}")
    print("------------------------------------------------------ \n")
  
  def add_Product_To_WishList(self,product):
    if product not in self.wishlist:
      product = product.lower()   
      self.wishlist.append(product)
      print("Product added in WishList")
    else:
      print("Product already present in WishList -------- Try other Products")

  def remove_Product_From_WishList(self,product):
    if product in self.wishlist:
      product = product.lower()
      self.wishlist.remove(product)
      print(f"{product} remove from wishlist")
    else:
      print(f'{product} not present in wishlist')
  
  def displayWishList(self):
    for prod in self.wishlist:
      print(f"------> {prod}")
    
  def updateEmail(self,new_email):
    self.email = new_email
  
  def updateAddress(self,new_addr):
    self.address = new_addr

# ------------------------------------------------------------

class Employee(Person):      # subclass of Person
  num_of_employee = 0        # class variable use to counts employees
  raise_amount = 1.04        # class variable use to raise basicpay

  def __init__(self,fname,lname,country,email,address,age,basicpay):
    super().__init__(fname,lname,age,country,email)

    self.firstName = firstName
    self.lastName = lastName

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
      # print(f"Desig of Employee is : {self.desig}")
      # print(f"Basic pay of Employee is : {self.basicpay}")

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

# ------------------------------------------------------------

class Developer(Employee):   # subclass of Employee
  def __init__(self,fname,lname,country,email,address,age,basicpay,prog_lang):
    super().__init__(fname,lname,age,country,email)
    self.prog_lang = prog_lang

# ------------------------------------------------------------

class Manager(Employee):     # subclass of Employee
  def __init__(self,fname,lname,country,email,address,age,basicpay,employee=None):
    super().__init__(fname,lname,country,email,address,age,basicpay)

    if employees is None:
      self.employees = []
    else:
      self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('------>', emp.fullname())

cust_1 = Customer("Test","User","Pakistan","test.user@example.com","ABC-Street",20,"iPhone 11")

cust_1.displayDetails()

Customer.total_customer

cust_2 = Customer("John","Kee","USA","john.kee@example.com","ABCD-Street",24,"Holo Lens")

Customer.total_customer

cust_2.add_Product_To_WishList('Google Daydream VR')

cust_2.add_Product_To_WishList("Nvidia GTX 1080")

cust_2.displayWishList()

cust_2.remove_Product_From_WishList("Nvidia GTX 1080")

cust_2.displayWishList()



