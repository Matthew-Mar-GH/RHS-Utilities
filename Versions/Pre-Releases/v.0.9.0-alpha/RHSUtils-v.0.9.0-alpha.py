import math
import os

current_grade = None
target_grade = None
final_weight = None
grade_needed = None

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

program_info = find("Program Info.txt", "C:/Users")
with open(program_info) as f:
    print(f.read())

while True:
    try:
        current_grade = float(input("What is your current grade? (All categories averaged).\n"))
    except ValueError:
        print("Error! Please enter a number!")
        continue
    if current_grade <= 0:
        print("Error! Please enter a positive number!")
    else:
        try:
            target_grade = float(input("What is your target grade after finals?\n"))
        except ValueError:
            print("Error! Please enter a number!")
            continue
        if target_grade <= 0:
            print("Error! Please enter a positive number!")
        else:
            try:
                final_weight = float(input("What is the weight of your final exam? Write as positive number without percent (15% would be 15).\n"))
            except ValueError:
                print("Error! Please enter a number!")
                continue
            if final_weight <= 0:
                print("Error! Please enter a positive number!")
                continue
            else:
                break

final_weight = final_weight/100
grade_needed = (target_grade - ((1-final_weight)*current_grade)) / (final_weight)
grade_needed = math.ceil(grade_needed)
if grade_needed > 100:
    grade_needed = str(grade_needed) + " (As it exceeds the maximum possible grade on the final, your target grade cannot be achieved.)"
elif grade_needed < 40:
    grade_needed = str(grade_needed) + " (As it is less than the minimum possible grade on the final (per RHS policy), your target grade is guaranteed to be achieved.)"
print(f"Current Grade: {current_grade}\nTarget Grade: {target_grade}\nFinal Weight: {100*final_weight}%\nGrade needed for a {target_grade}: {grade_needed}")
if_exit = str(input("Exit the program? (Type Y/N for Yes/No)"))
if if_exit == "Y":
    exit()

                    


