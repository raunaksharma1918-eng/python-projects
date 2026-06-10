#Q1: write a program that takes a number as input and prints
#   whether it is positive , negative or zero.

# sample input : 7
# sample input : positive

# num = int(input("Entyer your number"))
# if num > 0:
#       print("Postive")
# elif num < 0:
#       print("Negative")
# else:
#       print("zero")

# Sample Input : -3
#     Sample Output: Negative


# num = int(input("Entyer your number"))
# if num > 0:
#       print("Positive")
# elif num < 0:
#       print("negative")
# else:
#       print("zero")

# Sample Input : 0
#     Sample Output: Zero


# num = int(input("Entyer your number"))
# if num > 0:
#       print("Positive")
# elif num < 0:
#       print("negative")
# else:
#       print("zero")


# Q2: Write a program that takes two numbers as input and prints
#     the greater one. If both are equal, print "Both are equal".

#     Sample Input : 10 25
#     Sample Output: 25


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print("Both are equal")



# Sample Input : 7 7
#     Sample Output: Both are equal



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print("Both are equal")



# Q2: Take a number as input. If it is even, print "Even".
#     If it is odd, print "Odd".

#     Sample Input : 4
#     Sample Output: Even


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# Sample Input : 9
#     Sample Output: Odd


# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Q3: Write a program that takes a person's age as input.
#     If age is 18 or above, print "You can vote".
#     Otherwise print "You cannot vote".

#     Sample Input : 20
#     Sample Output: You can vote


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# else:
#     print("you cannot vote")



# Sample Input : 15
#     Sample Output: You cannot vote

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# else:
#     print("you cannot vote")



# Q4: Print all numbers from 1 to 20 using a loop.

#     Sample Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


# for i in range(1,21):
#     print(i, end=" ")


# Q5: Print all even numbers from 1 to 50 using a loop.

#     Sample Output: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50



# for i in range(1,51):
#     if i % 2 == 0:
#         print(i, end= " ")


#  Take a number n as input and print its multiplication
#     table (from 1 to 10).

#     Sample Input : 5
#     Sample Output:
#     5 x 1  = 5
#     5 x 2  = 10
#     5 x 3  = 15
#     5 x 4  = 20
#     5 x 5  = 25
#     5 x 6  = 30
#     5 x 7  = 35
#     5 x 8  = 40
#     5 x 9  = 45
#     5 x 10 = 50


# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")



    