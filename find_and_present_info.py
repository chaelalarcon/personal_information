def search_and_display_information():
    while True:
        try:
            find_name = input("Enter the full name to search for: ").strip()

            if any(char.isdigit() for char in find_name):
                print("Error: Full name should not contain numbers. Please enter a valid name.")
                continue  # Ask for input again if invalid
            
              # Open the file and search for the full name
            found = False
            with open("personal_information.txt", "r") as file:
                lines = file.readlines()  # Read all lines at once

            for i in range(len(lines)):
                    # Check if the current line starts with the full name
                    if lines[i].startswith(f"Full Name: {find_name}"):
                        found = True
                        print("\nInformation found:")
                        # Print the information for the found full name
                        print(lines[i].strip())  # Print the full name line
                        # Print the subsequent information
                        if i + 1 < len(lines): print(lines[i + 1].strip())  # Age
                        if i + 2 < len(lines): print(lines[i + 2].strip())  # Birthday
                        if i + 3 < len(lines): print(lines[i + 3].strip())  # Year Level
                        if i + 4 < len(lines): print(lines[i + 4].strip())  # Program
                        if i + 5 < len(lines): print(lines[i + 5].strip())  # Section
                        break  # Stop once the information is found
            
            if not found:
                    print(f"No information found for {find_name}. Please try again.")

            # Ask if the user wants to search for another name
            continue_search = input("\nWould you like to search for another person? (yes/no): ").strip().lower()
            if continue_search == "no":
                print("Exiting the search program...")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

def main():
    search_and_display_information()

main()
