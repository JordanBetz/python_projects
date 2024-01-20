#### Leicht
# 1. **Rechner für den Body-Mass-Index (BMI)**: Berechne den BMI.
try:

    kg = float(input("What's your weight in (kg)?: "))
    user_height = input("What's your height in (m)?: ")
    height = float(user_height.replace(',', '.'))

    bmi = round(kg/(height**2))
    print(bmi)

except ValueError as e:
    print(f"ERROR: {e}")


