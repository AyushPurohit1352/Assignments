import json

DATA_FILE = 'students.json'
ADMIN_PASSWORD = 'admin123'

FEE_STRUCTURE = {
    1: 50000,
    2: 52000,
    3: 54000,
    4: 56000
}
SCHOLARSHIP_PERCENTAGE = 35

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def admin_dashboard():
    students = load_data()

    print("\n--- Admin Dashboard ---")

    print("\nStudents who have Paid Fees:")
    for student in students:
        if student['fee_paid']:
            print(f"{student['name']} (Roll Number: {student['roll_number']}) - Year {student['year']}")

    print("\nDefaulters (Have not Paid Fees):")
    for student in students:
        if not student['fee_paid']:
            print(f"{student['name']} (Roll Number: {student['roll_number']}) - Year {student['year']}")

    print("\nAdmin Menu")
    print("1. Add Student")
    print("2. Generate Report")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        generate_report()
    elif choice == '3':
        print("Exiting Admin Menu.")
    else:
        print("Invalid choice, please try again.")

def add_student():
    students = load_data()
    
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    year = int(input("Enter student's year: "))
    percentage = float(input("Enter student's percentage: "))
    fee_paid = False

    student = {
        "name": name,
        "roll_number": roll_number,
        "year": year,
        "percentage": percentage,
        "fee_paid": fee_paid
    }
    
    students.append(student)
    save_data(students)
    print(f"Student {name} added successfully!")

def generate_report():
    students = load_data()
    report = []
    
    for student in students:
        status = "Paid" if student['fee_paid'] else "Not Paid"
        report.append({
            "Name": student['name'],
            "Roll Number": student['roll_number'],
            "Year": student['year'],
            "Status": status
        })
    
    with open('fee_report.json', 'w') as report_file:
        json.dump(report, report_file, indent=4)
    
    print("Report generated successfully! Check 'fee_report.json'")

def student_menu(roll_number):
    students = load_data()
    
    student = next((s for s in students if s['roll_number'] == roll_number), None)
    
    if not student:
        print("Student not found.")
        return
    
    print(f"\nWelcome, {student['name']} (Year: {student['year']})")
    
    if student['fee_paid']:
        print("You have already paid the fees.")
    else:
        year = student['year']
        percentage = student['percentage']
        base_fee = FEE_STRUCTURE[year]
        tuition_fee = base_fee - 10000
        development_fee = 10000
        final_fee = base_fee
        
        print(f"\nFee Structure for Year {year}:")
        print(f"Tuition Fees: {tuition_fee}")
        print(f"Development Fees: {development_fee}")
        print(f"Total Fees: {base_fee}")

        if percentage >= 95:
            discount = (SCHOLARSHIP_PERCENTAGE / 100) * base_fee
            final_fee -= discount
            print(f"Scholarship Applied: {SCHOLARSHIP_PERCENTAGE}%")
        
        print(f"Total Fee to Pay after Scholarship (if applicable): {final_fee}")

        choice = input("Would you like to pay the fees now? (yes/no): ").lower()
        if choice == 'yes':
            student['fee_paid'] = True
            save_data(students)
            print("Fees paid successfully!")
        else:
            print("You chose not to pay the fees.")

def student_login():
    roll_number = input("Enter your roll number: ")
    student_menu(roll_number)

def main():
    while True:
        print("\nFee Management System")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")
        
        choice = input("Enter your role (1-3): ")
        
        if choice == '1':
            password = input("Enter Admin Password: ")
            if password == ADMIN_PASSWORD:
                while True:
                    admin_dashboard()
                    exit_choice = input("Do you want to exit Admin interface? (yes/no): ").lower()
                    if exit_choice == 'yes':
                        break
            else:
                print("Invalid password!")
        
        elif choice == '2':
            student_login()
        
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
