m = (float(input("Your height(m):")))
kg = int(input("Your weight(kg):"))
bmi = kg // (m * m)
print("Your BMI:", bmi)
if bmi < 16:
    print("You're sevelery underweight")
elif 16 < bmi <18.5:
    print("You're underweight")
elif 18.5 < bmi <25:
    print("You're normal")
elif 25 < bmi <30:
    print("You're overweight")
else:
    print("Your're obese")