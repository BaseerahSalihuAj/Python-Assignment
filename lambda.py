num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#list comprehension to get the square of the prime numbers
squares = [x**2 for x in num if x > 0 and x < 20 if x % 2 == 1]
primes = [n for n in num if all (n % i != 0 for i in range (2,n)) and n>1]

print(squares) 
print(primes) 

# question 1
#given list of words
worlds = ["hello", "world", "lambda", "map"]
capitalized_world = [world.capitalize() for world in worlds]

print(capitalized_world)


# question 2
#given a list of string, create a new list containing only the strings that have a length greater than a specified threshold (4)

strings = ["hello", "world", "lambda", "map", "tuples", "string", "function"]
strings = [ world for world in worlds if len (world) > 4]


print(strings)


# question 3
# given a range of numbers,create a list of tuples
# where each tuple contains thenumber and its cube


tuples_list = [1,2,3,4,5,6,7]
new_tuple_list = [(num**3) for num in tuples_list ]

print(new_tuple_list)

#question 4
# write a program that prints numbers from 1 to 100.
# for multiples of 3, print "fizz" instead of the number.
#for multiples of 5, print "buzz" instead of the number.
# for multiples of both 3 and 5, print "fizzbuzz" instead of the number.


number = range (1, 101)
def multiples_of_number(number):
    for i in range(1, 101):
        if i % 15 == 0:
            print ("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
print (multiples_of_number(number))