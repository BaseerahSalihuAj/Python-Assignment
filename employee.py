# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    

#     def  change_salary(self,amount):
#         self.salary += amount
    

# #create employee instance


# employees = [
#     Employee("Alice",50000),
#     Employee("Bob",60000),
#     Employee("Charlie",70000),
#     Employee("Avast",2000)
# ]


# #Change the salaries by 10k
# for employee in employees:
#     if employee.name != "Avast":
#         employee.change_salary(10000)


# for employee in employees:
#     print(f"{employee.name}'s new salary:{employee.salary}")

class  Dog:
    __number = 0
    #_protected = "i am a protected  variable"
    def __init__(self,name):
        self.name = name
        Dog.__number += 1
        self.dognumber = Dog.__number

        def bark(self):
            print(f"{self.name}says woof")
jack = Dog("jack")
print(jack.dognumber)
bingo = Dog("bingo")
print(bingo.dognumber)


class Account:
    def __init__(self,balance):
    #getter method
    @property
    def balance(self):
        return self._balance   

    #setter method
    @balance.setter
    def balance(self,number):
     self.__balance = number