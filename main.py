weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))
body_mass_index = weight / (height ** 2)
bmi = round(body_mass_index, 1)
print(f"Your body mass index is {bmi}")
if bmi < 16.0:
    print("Underweight (Severe thinness)")
elif bmi < 16.9:
    print("Underweight (Moderate thinness)")
elif bmi < 18.4:
    print("Underweight (Mild thinness)")
elif bmi < 24.9:
    print("Normal range")
elif bmi < 29.9:
    print("Overweight (Pre-obese)")
elif bmi < 34.9:
    print("Obese (Class 1)")
elif bmi < 39.9:
    print("Obese (Class 2)")
else:
    print("Obese (Class 3")
