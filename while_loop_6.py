""" while Loop """

a = 0
while a < 15:
    print(a)
    a += 2

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1    


# Nested while loop
for x in range(2, 10):
  for k in range(1, 5):
    print(x, k, end = " ")   

# while loop with break and continue
score = 1
while score < 15:
    score += 1    
    if score ==11:
      break      
    print(f"Your score is {score}")   

    
# while loop with  continue

location = 5
while location < 20:
    location += 1
    if location == 11:
      continue
    print(f"You had stayed in this house location {location} in the past 20 years") 

# for num in range(10, 14):
#     for i in range(2, num):
#         if num%i == 1:
#             print(num)
#             break    
