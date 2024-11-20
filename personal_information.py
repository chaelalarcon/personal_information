def collect_information():
    while True: 
        try: 
            # Ask the user for their personal information
            full_name = input("Enter your full name: ")
            age = int(input("Enter your age: "))
            birthday = int(input("Enter your birthday (MM-DD-YYYY): "))
            year_level = input("Enter your year level (in words): ")
            program = input("Enter your program: ")
            section = int(input("Enter your section: "))

            # Validation for the birthday using split and length check
            parts = birthday.split('-')
            if len(birthday) != 3:
                print ("Error: Follow the date format (MM-DD-YYYY)")
                continue    # Ask for the user to input again
            
            year, month,day = parts 
            if len(year) != 4 or not year.isdigit() or not month.isdigit() or not day.isdigit():
                print("Error: Follow the date format (MM-DD-YYYY)")
                continue    # Ask for the user to input again

            # Return the gathered information as a formatted string: 
            return f"Full Name: {full_name}\nAge: {age}\nBirthday: {birthday}\nYear Level: {year_level}\nProgram: {program}\nSection: {section}"
        
        except Exception as e:
            print(f"An error occured while gathering the information: {e} ")
            continue

def main():
    while True:
        # Collect the information from the user
        user_info = collect_information()

        if user_info is None: 
            continue    # Skip writing the file if there was an error in collecting information