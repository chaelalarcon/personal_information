def collect_information():
    while True: 
      
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
            
            