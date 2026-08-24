def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 16:
        return "Severely Underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class 1"
    else:
        return "Obese Class 2"

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_result(name, weight, height_cm, bmi, category):
    print("\n" + "="*40)
    print(f"           BMI REPORT - {name}")
    print("="*40)
    print(f"Height       : {height_cm} cm")
    print(f"Weight       : {weight} kg")
    print(f"BMI          : {bmi}")
    print(f"Category     : {category}")
    print("="*40)

def main():
    print("Welcome to the BMI Calculator!")
    
    history = []
    
    while True:
        name = input("\nEnter your name: ")
        weight = get_valid_input("Enter your weight in kg: ")
        height_cm = get_valid_input("Enter your height in cm: ")
        
        bmi = calculate_bmi(weight, height_cm)
        category = get_category(bmi)
        
        display_result(name, weight, height_cm, bmi, category)
        
        history.append({"name": name, "bmi": bmi, "category": category})
        
        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            break
    
    print("\n--- Session History ---")
    for record in history:
        print(f"{record['name']}: BMI = {record['bmi']} ({record['category']})")
    
    print("\nThank you for using the BMI Calculator!")

if __name__ == "__main__":
    main()
