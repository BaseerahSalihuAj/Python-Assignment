# import random
# number = random.randrange(1,10)
# while number != 0:
#     guess = int(input("make your guess:"))
#     if guess < number:
#         print("Too low")
#     elif guess > number:
#         print("Too high")
#     else:
#         print("You guessed it right!!")
#         break
#     number -= 1

# for number in range(2,10,2):
#     print(number)

# def test():
#     global food
#     food = ['eba','amala','indomie','eggs']
#     for i in range(len(food)) :
#         print(i,food[i])
# test()    


# def area(length,breadth):
#     return length*breadth
# print(area 4*5)


def calculate_simple_interest(principal,rate,time):
    simple_interest = (principal*rate*time)/100
    return simple_interest
print(  calculate_simple_interest(1000,4,60))


def simple_interest_calculator(principal:int,rate:int,time:int):

    # principal = int(input("enter value for principal"))
    # rate = int(input("Enter value for rate"))
    # time = int(input("Enter value for time"))
    if rate <= 100:
        simple_interest = (principal * rate * time)/100
        return simple_interest
    else:
        return ("Enter valid input for rate")
    
