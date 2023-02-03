# percentage = int(input("Enter your percentage: "))

# if percentage < 60: print("D")
# elif (percentage >= 60 and percentage <= 80) : print("C")
# elif (percentage > 80 and percentage <= 90) : print("B")
# elif (percentage > 90) : print("A")


# costPrice = int(input("Enter cost price: "))
# if costPrice <= 50000:
#     print("Tax: ", (5/100) * costPrice)
# elif (costPrice > 50000 and costPrice <= 100000):
#     print("Tax: ", (10/100) * costPrice)
# else:
#     print("Tax: ", (15/100) * costPrice)

# city = input("Enter City: ").title()

# dict = {
#     "Delhi": "Red Fort",
#     "Agra": "Taj Mahal",
#     "Jaipur": "Jal Mahal"
# }

# print(city + ":", dict[city] if city in dict else "Error 404", city)

# ? Check how many times a given number can be divided by 3 before it is less than or equal to 10.

# num = int(input("Enter the number: "))
# value = num
# count = 0

# while value >= 10:
#   value /= 3
#   count += 1

# print(str(count) + " times")

# if count print(num, ("÷3 " * count) + " = " + str(value)[:4])

# ? Use nested while loop to print 3 differnt patterns.

# # ========================#
# #! Pattern-1 :

# i = 7

# while i > 1:
#   i -= 1
#   j = i
#   while j > (i - 1):
#     j -= 1
#     print("• " * j)


# # ========================#
# #! Pattern-2 :

# i = 8
# while i>1:
#   i -= 1
#   j = 10;
#   while j>0:
#     j -= 1
#     if ((j > 2) and (j < 7) and (i!=4)):
#       print(" ", end="")
#       continue
#     print("@", end="")
#   print("")


# # ========================#
# #! Pattern-2 :

# i = 5
# j = 5

# while i > 0:
#     i -= 1
#     while j > 0:
#         j -= 1
#         print("+"*(i*j), end="")
#     print("")

# i = 10

# while i>0:
#     print(i)
#     i -= 1

i = 0

while i<10:
    print(10-i)
    i += 1
