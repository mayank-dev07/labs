# import random

# Choice = ["Rock","Paper","Scissors"]

# Comp = random.choice(Choice)

# print("1 for Rock, 2 for Paper, 3 for scissors")
# ch = input("enter choice")
# match ch:
#     case "1":
#         print("Your choice is Rock")
#         print("Computer choosed",Comp)
#         if(Comp == "Rock"):
#             print("Tie")
#         elif(Comp == "Paper"):
#             print("Comp win")
#         else:
#             print("You win")
#     case "2":
#         print("Your choice is Paper")
#         print("Computer choosed",Comp)
#         if(Comp == "Rock"):
#             print("You Win")
#         elif(Comp == "Paper"):
#             print("Tie")
#         else:
#             print("Comp Win")
#     case "3":
#         print("Your choice is Scissor")
#         print("Computer choosed",Comp)
#         if(Comp == "Rock"):
#             print("Comp win")
#         elif(Comp == "Paper"):
#             print("You Win")
#         else:
#             print("Tie")
#     case default:
#         print("Enter valid choice")




# import math

# lst = []
# n = int (input("enter value"))
# for i in range(0,n):
#     element = int(input())
#     lst.append(element)

# for i in range(0,n):
#     D = lst[i]
#     print(int(math.sqrt((2*50*D)/30)))



input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split(',')
sorted_words = sorted(words)
sorted_sequence = ",".join(sorted_words)
print("Sorted sequence:", sorted_sequence)