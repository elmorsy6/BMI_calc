# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmiCalc = float(weight) / float(height) ** 2
print("{:.2f}".format(bmiCalc))