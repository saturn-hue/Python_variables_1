""""Control flow logic"""

# if condition


age = int(input("Enter your age:  "))
#print("You are an adult",  age)

if age >= 60 :
    print("You need medical check up every year with your doctor")
elif age <= 60 and age >= 50:
    print("Watch what you eat daily")
elif age <= 50 and age >= 20:
    print("You are in good health, keep it up")
else:
    print("You are a child, enjoy your life")