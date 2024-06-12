list_of_employee = [
    { 
        'name': 'Maryam',
     'details':{
         'age': '10',
         'task':['surgery','delivery'],
         'position': 'Doctor'
     }

    } ,
    { 
        'name':'Basirah',
     'details':{
         'age': '30',
         'task':['Coding', 'Debuging'],
         'position': 'Developer'
     }

    } ,
    { 
        'name':'Aisha',
     'details':{
         'age':'15',
         'task':['Xray','Ultrasound'],
         'position':'Radiologist'
     }

    } ,
    { 
        'name':'Halimah',
     'details':{
         'age':'25',
         'task':['Research','Diagnosis'],
         'position':'Microbiologist'
     }

    } ,
 { 
    'name':'Zainab',
     'details':{
         'age': '15',
         'task':['Deposit','Withdrawal'],
         'position':'Banker'
     }

    } 
]
print(list_of_employee[0]['details']['task'][0])

for employee in list_of_employee:
    print((employee["name"]).upper())


list_instance = [1,2,3,4]
iterator = iter(list_instance)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


def factors(n):
    for val in range(1, n+1):
        if n % val == 0:
            yield val
factors_of_20 = factors(20)
print(next(factors_of_20))

print((val for val in range(1,20+1)if n % val == 0))



def employee_name(list_of_employee):
    for employee in list_of_employee:
        yield employee["name"]

print(employee_name(employee))