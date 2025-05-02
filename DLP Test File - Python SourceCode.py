# Confidential: This script contains sensitive logic for internal use only.

def calculate_salary(employee_id):
    # Confidential formula, do not share externally
    base_salary = 50000
    bonus = 0.10
    total = base_salary + (base_salary * bonus)
    print(f"Confidential: Calculating salary for employee {employee_id}")
    return total

def main():
    employee_id = "EMP1234"
    salary = calculate_salary(employee_id)
    print(f"Final salary for {employee_id} is ${salary}")

if __name__ == "__main__":
    main()