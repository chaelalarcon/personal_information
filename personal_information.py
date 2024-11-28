def collect_information():
    while True: 
        try: 
            # Ask the user for their personal information
            full_name = input("Enter your full name: ")

            # Ensure the full name doesn't contain numbers
            if any(char.isdigit() for char in full_name):
                print("Error: Full name should not contain numbers. Please enter a valid name.")
                continue  # Ask for the user to input again

            age = int(input("Enter your age: "))

            if age <= 0:
                print("Error: Age must be a positive number greater than 0. Please enter a valid age.")
                continue  # Ask for the user to input again

            # Validation for the birthday
            birthday = input("Enter your birthday (MM-DD-YYYY): ")

            # Split the birthday input by '-' to separate the month, day, and year
            parts = birthday.split('-')
            if len(parts) != 3:
                print("Error: Follow the date format (MM-DD-YYYY).")
                continue  # Ask for the user to input again

            month, day, year = parts

            # Check if the month, day, and year are valid integers
            if not (month.isdigit() and day.isdigit() and year.isdigit()):
                print("Error: Month, day, and year must be numeric.")
                continue  # Ask for the user to input again

            # Check that month is between 01 and 12
            if not (1 <= int(month) <= 12):
                print("Error: Month must be between 01 and 12.")
                continue

            # Check that day is within valid range for the month (basic validation, not considering leap years)
            if not (1 <= int(day) <= 31):
                print("Error: Day must be between 01 and 31.")
                continue

            # Check that year is a 4-digit number
            if len(year) != 4:
                print("Error: Year must be a 4-digit number.")
                continue

            # Get the year level and ensure it contains no numbers
            year_level = input("Enter your year level (in words): ")

            if any(char.isdigit() for char in year_level):  # Check if there are any digits
                print("Error: Year level should not contain numbers. Please enter a valid year level (e.g., Freshman).")
                continue  # Ask for the user to input again

            # Get the program and ensure it contains no numbers
            program = input("Enter your program: ")

            if any(char.isdigit() for char in program):  # Check if there are any digits
                print("Error: Program should not contain numbers. Please enter a valid program name.")
                continue  # Ask for the user to input again

            # Get the section number and validate it is positive
            section = int(input("Enter your section: "))
            
            if section <= 0:
                print("Error: Section must be a positive number. Please enter a valid section.")
                continue  # Ask for the user to input again

            # Return the gathered information as a formatted string: 
            return f"Full Name: {full_name}\nAge: {age}\nBirthday: {birthday}\nYear Level: {year_level}\nProgram: {program}\nSection: {section}"
        
        except Exception as e:
            print(f"An error occurred while gathering the information: {e}")
            continue

def main():
    while True:
        try:
            # Collect the information from the user
            user_info = collect_information()

            if user_info is None: 
                continue    # Skip writing the file if there was an error in collecting information

            try:
                with open("personal_information.txt", "a") as file:
                    file.write(user_info + "\n")
                print("Information saved successfully.")
            
            except IOError as e:
                print(f"Error: Failed to add the file: {e}")

            # Ask the user if they want to continue or exit 
            continue_input = input("Would you like to input another person? (yes/no): ").strip().lower()
            if continue_input == 'no':
                print("Exiting the program...")
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()
