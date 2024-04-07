from function import Function  # Import the Function class from the function module

class UserInterface:
    def __init__(self):
        self.function_object = Function()  # Initialize a Function instance to handle team operations

    def display_menu(self):
        # Display menu options until the user chooses to exit
        while True:
            print("\nMenu:")
            print("1. Create Team")  # Option to create a new team
            print("2. Read Teams")   # Option to display existing teams
            print("3. Update Team")  # Option to update team details
            print("4. Delete Team")  # Option to delete a team
            print("5. Show Team Statistics") # Option to display statistics about the teams
            print("6. Cancel A Team") # Option to Cancel a team and display the cancelled date
            print("7. Save team information as txt file") # Option to save team information as txt file in my folder
            print("8. Restore team information from txt file") # Option to restore team information from txt file in my folder
            print("9. Exit")         # Option to exit the program
            # Prompt the user to choose an option
            choice = input("\nEnter your choice (1-9): ")
            # Process the user's choice
            if choice == '1':
                self.function_object.create_team()  # Invoke the method to create a new team
            elif choice == '2':
                self.function_object.read_team()    # Invoke the method to display existing teams
            elif choice == '3':
                self.function_object.update_team()  # Invoke the method to update team details
            elif choice == '4':
                self.function_object.delete_team()  # Invoke the method to delete a team
            elif choice == '5':
                self.function_object.team_statistics()  # Invoke the method to show team statistics
            elif choice == '6':
                self.function_object.cancel_team_participation()  # Invoke the method to show Cancelled team details
            elif choice == '7':
                self.function_object.save_teams_to_file()  # Invoke the method to save the file in current directory
            elif choice == '8':
                self.function_object.restore_teams_from_file()  # Invoke the method to restore the file in current directory
            elif choice == '9':
                print("Exiting program.")  # Display exit message
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please try again.")  # Display message for invalid input
