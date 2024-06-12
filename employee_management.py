class Employee:
    def _init_(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

class company:
    def _init_(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        employee = Employee(name, age, position, salary)
        self.employees.append(employee)
        print("Employee added successfully!")

    def remove_employee(self):
        name = input("Enter employee name to remove: ")
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("Employee removed successfully!")
                return 
        print("Employee not found.")

    
    def update_employee(self):
        name = input("Enter employee name to update: ")
        for employee in self.employees:
            if employee.name == name:
                employee.position = input("Enter new position: ")
                employee.salary = float(input("Enter new salary: "))
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def view_all_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")

    def find_employee_by_name(self):
        name = input("Enter employee name to find: ")
        for employee in self.employees:
            if employee.name == name:
                print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")
                return
        print("Employee not found.")

def user_interface():
    ems = company()
    while True:
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update employee")
        print("4. View all employees")
        print("5. Find employee by name")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            ems.add_employee()
        elif choice == "2":
            ems.remove_employee()
        elif choice == "3":
            ems.update_employee()
        elif choice == "4":
            ems.view_all_employees()
        elif choice == "5":
            ems.find_employee_by_name()
        elif choice == "6":
            break
        else:
            
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    user_interface ()
      