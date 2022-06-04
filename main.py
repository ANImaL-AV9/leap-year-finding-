# 🚨 Don't change the code below 👇

# 🚨 Don't change the code above 👆

#Write your code below this line
year = int(input("Which year do you want to check? "))
if year % 4==0:
  if year%100!=0:
    if year%400==0:
      print(f"the {year} is leap year")
    else:
      print(f"the {year} is not leap year.")
  else:
    print(f"the {year} is a leap year.")
else:
  print(f"the {year} is not a leap year.")