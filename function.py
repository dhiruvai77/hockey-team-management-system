# Import the parent class Team
from team import Team
# Import the datetime module to work with dates and time
import datetime
# Import the os module for working with file paths
import os

#Create a class called function to define the functions required for operations
class Function:
    def __init__(self):
        self.team_list = []  # Initialize an empty list to store teams

    def create_team(self):
        while True:
            # Ask user for team details
            # Ask user for team name
            name = str(input("\nPlease enter the name of the team:\n "))          
            #Ask user to enter the type of the team
            team_type = str(input("Please enter 'Boy' if it's a boy team and 'Girl' if it's a girls team:\n ")).capitalize()
            while team_type not in ['Boy', 'Girl']:
                print("Invalid team type. Please enter 'Boy' or 'Girl'.")
                team_type = input("Please enter 'Boy' if it's a boy team and 'Girl' if it's a girls team:\n ").capitalize()            
            # Ask user for fee payment status
            fee_paid = input("Please enter '1' if the fee is already paid and '0' if it's not paid:\n ")
            while fee_paid not in ['0', '1']:
                print("Invalid input. Please enter either '0' or '1'.")
                fee_paid = input("Please enter '1' if the fee is already paid and '0' if it's not paid:\n ")
            # Convert fee payment input to appropriate format
            fee_paid = "Paid" if fee_paid == '1' else "Not Paid"           
            # Ask user for fee amount required for registration
            while True:
                fee_amount = input("Please enter the fee amount required for registration:\n ")
                if fee_amount.isdigit():
                    break
                print("Invalid input. Please enter a numeric value.\n")            
            # Create a Team object with the provided details and append it to the team list
            object_team = Team(name, team_type, fee_paid, fee_amount)
            self.team_list.append(object_team)
            print("\nTeam created successfully.")
            # Ask the user if they want to continue creating teams
            another = input("Do you want to create another team? (yes/no): ").lower()
            if another != 'yes':
                break

    #Function to display the teams created
    def read_team(self):
        while True:
            # Display menu options
            print("\nChoose an option:\n1. Display all teams\n2. View team by ID\n3. View team by type (boy/girl)\n4. Return to main menu\n")
            # Ask for input
            option = input("Enter option: ")
            # Based upon option selected perform the task
            if option == '1':
                # Display all teams if available
                if self.team_list:
                    print("All teams:")
                    for object_team in self.team_list:
                        # Print details of each team
                        print("\nTeam ID:", object_team.get_id())
                        print("Date Created:", object_team.get_date_created())
                        print("Name:", object_team.get_name())
                        print("Type of team:", object_team.get_team_type())
                        print("Payment Status:", object_team.get_fee_paid())
                        print("Amount to be Paid:", object_team.get_fee_amount())
                        cancellation_date = object_team.get_cancellation_date()
                        if cancellation_date:
                            print("Cancellation Date:",cancellation_date)
                else:
                    print("No teams available.")
            elif option == '2':
                # View team details by ID
                team_id = input("\nEnter Team ID to view information: ")
                # Validate input
                if not team_id.isdigit():
                    print("Invalid input. Please enter a numeric value.")
                    continue
                team_id = int(team_id)
                found = False
                # Search for team by ID
                for object_team in self.team_list:
                    if object_team.get_id() == team_id:
                        found = True
                        # Print details of the found team
                        print("\nTeam ID:", object_team.get_id())
                        print("Date Created:", object_team.get_date_created())
                        print("Name:", object_team.get_name())
                        print("Type of team:", object_team.get_team_type())
                        print("Payment Status:", object_team.get_fee_paid())
                        print("Amount to be Paid:", object_team.get_fee_amount())
                        cancellation_date = object_team.get_cancellation_date()
                        if cancellation_date:
                            print("Cancellation Date:",cancellation_date)
                        break
                if not found:
                    print("Team not found.")
            elif option == '3':
                # View teams by type (boy/girl)
                team_type_filter = input("Enter team type ('Boy' or 'Girl') to filter team_list: ").capitalize()
                # Validate input
                while team_type_filter not in ['Boy', 'Girl']:
                    print("Invalid team type. Please enter 'Boy' or 'Girl'.")
                    team_type_filter = input("Enter team type ('Boy' or 'Girl') to filter team_list: ").capitalize()
                filtered_team_list = [object_team for object_team in self.team_list if object_team.get_team_type() == team_type_filter]
                if filtered_team_list:
                    # Display teams of the specified type
                    print("Teams of type ",team_type_filter)
                    for object_team in filtered_team_list:
                        # Print details of each team
                        print("\nTeam ID:", object_team.get_id())
                        print("Date Created:", object_team.get_date_created())
                        print("Name:", object_team.get_name())
                        print("Type of team:", object_team.get_team_type())
                        print("Payment Status:", object_team.get_fee_paid())
                        print("Amount to be Paid:", object_team.get_fee_amount())
                        cancellation_date = object_team.get_cancellation_date()
                        if cancellation_date:
                            print("Cancellation Date:",cancellation_date)
                else:
                    print("No Teams of type",team_type_filter, "found.")
            elif option == '4':
                # Return to main menu
                print("Returning to main menu.")
                break
            else:
                print("Invalid option.")

    # Function to update team details
    def update_team(self):
        # Iterate until the user finishes updating teams
        while True:
        # Update team details by ID
            team_id = input("\nPlease enter the ID of the team you want to update: ")
            # Check if the input is numeric
            if not team_id.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue
            team_id = int(team_id)
            team_found = False          
            # Search for the team with the provided name
            for object_team in self.team_list:
                if object_team.get_id() == team_id:
                    team_found = True
                    # Enter a loop to handle different update options
                    while True:
                        print("\nWhich attribute do you want to update?")
                        print("1. Name")
                        print("2. Team Type")
                        print("3. Payment Status")
                        print("4. Amount to be Paid")
                        print("5. Finish Update")
                        choice = input("\nEnter your choice (1/2/3/4/5): ")                       
                        # Check if the choice is valid
                        if choice not in ['1', '2', '3', '4', '5']:
                            print("Invalid choice!")
                            continue
                        # Update the selected attribute according to the choice
                        if choice == '1':
                            new_name = input("Enter the new Name for the Team: ")
                            object_team.set_name(new_name)
                            print("Name is updated successfully!")                          
                        elif choice == '2':
                            new_team_type = input("Enter the new type of the Team ('Boy' or 'Girl'): ").capitalize()
                            while new_team_type not in ['Boy', 'Girl']:
                                print("Invalid team type. Please enter 'Boy' or 'Girl'.")
                                new_team_type = input("Enter the new type of the Team ('Boy' or 'Girl'): ").capitalize()
                            object_team.set_team_type(new_team_type)
                            print("Type of Team is updated successfully!")                          
                        elif choice == '3':
                            new_fee_paid = input("Enter the new payment Status ('1' for paid and '0' for unpaid): ")
                            while new_fee_paid not in ['0', '1']:
                                print("Invalid input. Please enter either '0' or '1'.")
                                new_fee_paid = input("Enter the new payment Status ('1' for paid and '0' for unpaid): ")
                            object_team.set_fee_paid("Paid" if new_fee_paid == '1' else "Not Paid")
                            print("Payment Status updated successfully!")                           
                        elif choice == '4':
                            new_amount = input("Enter the updated amount: ")
                            while not new_amount.isdigit():
                                print("Invalid input. Please enter a numeric value.")
                                new_amount = input("Enter the updated amount: ")
                            object_team.set_fee_amount(new_amount)
                            print("Amount updated successfully!")                           
                        elif choice == '5':
                            print("Update is completed")
                            break
                    break          
            # If the team with the provided name is not found, prompt the user to check the ID and try again
            if not team_found:
                print("Team not found. Please check the ID and try again.")
            another = input("Do you want to update another team? (yes/no): ").lower()
            if another != 'yes':
                break

    # Function to delete any teams based on their team ID
    def delete_team(self):
        # Iterate until the user finishes deleting teams
        while True:
            # Prompt the user to enter the ID of the team to delete
            team_id = input("Enter the ID of the team to delete: ")
            # Check if the input is numeric
            if not team_id.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue
            team_id = int(team_id)
            team_found = False
            # Search for the team with the provided ID
            for i, object_team in enumerate(self.team_list):
                if object_team.get_id() == team_id:
                    team_found = True
                    # Delete the team from the list
                    del self.team_list[i]
                    print("Team deleted successfully.")
                    break
            # If the team is not found, notify the user to check the ID and try again
            if not team_found:
                print("Team not found. Please check the ID and try again.")
            another = input("Do you want to delete another team? (yes/no): ").lower()
            if another != 'yes':
                break

    # Function to display the team statistics such as total teams and % of teams that have payed fees
    def team_statistics(self):
        # Calculate total number of teams
        total_teams = len(self.team_list)
        # Calculate the number of teams that have paid their fee
        paid_teams = sum(1 for object_team in self.team_list if object_team.get_fee_paid() == "Paid")
        # Display team statistics
        print("\nTeam Statistics:")
        print("Total teams:", total_teams)
        # Calculate and display the percentage of teams that have paid their fee
        print("Percentage of teams that have paid their fee:", (paid_teams / total_teams) * 100 if total_teams != 0 else 0, "%")

    def cancel_team_participation(self):
        # Prompt user to enter the ID of the team to cancel participation for
        team_id = int(input("Enter the ID of the team you want to cancel participation for: "))      
        # Find the team object with the given ID
        object_team = next((object_team for object_team in self.team_list if object_team.get_id() == team_id), None)      
        # Check if the team object exists
        if object_team:
            # Prompt user to enter the cancellation date
            cancellation_date_str = input("Enter the cancellation date (YYYY-MM-DD): ")
            cancellation_date = datetime.datetime.strptime(cancellation_date_str, "%Y-%m-%d")          
            # Set the cancellation date for the team
            object_team.set_cancellation_date(cancellation_date)           
            # Print confirmation message
            print("Team participation successfully canceled.")           
            # Get a list of canceled teams
            canceled_teams = [object_team for object_team in self.team_list if object_team.get_cancellation_date() is not None]           
            # Check if there are any canceled teams
            if canceled_teams:
                print("\nCanceled Team:")
                # Print details of each canceled team
                for object_team in canceled_teams:
                    print("Team ID: ",object_team.get_id())
                    print("Date Created: ",object_team.get_date_created())
                    print("Name: ",object_team.get_name())
                    print("Team Type: ",object_team.get_team_type())
                    print("Payment Status: ",object_team.get_fee_paid())
                    print("Amount to be Paid: ",object_team.get_fee_amount())
                    print("Cancellation Date: ",object_team.get_cancellation_date())
            else:
                print("No teams have been canceled.")
        else:
            print("Team not found with the provided ID.")
            
    # Function to save the information of teams to a text file
    def save_teams_to_file(self):
        # Get the directory path of the current Python script
        folder_path = os.path.dirname(os.path.abspath(__file__))
        # Prompt the user to enter the name of the file to save teams information
        file_name = input("Enter the name of the file to save teams information: ")
        # Append the file extension .txt if not provided by the user
        file_name += ".txt"
        # Construct the full file path by joining the folder path and file name
        file_path = os.path.join(folder_path, file_name)
        try:
            # Open the file in write mode
            with open(file_path, 'w') as file:
                # Write the header line
                file.write("Team ID,Date Created,Name,Team Type,Payment Status,Amount to be Paid,Cancellation Date\n")
                # Iterate over each team object in the team list
                for object_team in self.team_list:
                    # Write team information to the file as comma-separated values
                    file.write(f"{object_team.get_id()},")  # Team ID
                    file.write(f"{object_team.get_date_created()},")  # Date Created
                    file.write(f"{object_team.get_name()},")  # Team Name
                    file.write(f"{object_team.get_team_type()},")  # Team Type
                    file.write(f"{object_team.get_fee_paid()},")  # Payment Status
                    file.write(f"{object_team.get_fee_amount()},")  # Amount to be Paid
                    cancellation_date = object_team.get_cancellation_date()  # Cancellation Date
                    if cancellation_date:
                        # Format cancellation date
                        formatted_cancellation_date = cancellation_date.strftime("%Y-%m-%d %H:%M:%S")
                        file.write(formatted_cancellation_date)  # Write formatted cancellation date
                    file.write("\n")  # Add a new line after each team
            # Print success message
            print("Teams information saved to .txt file successfully.")
        except IOError as e:
            # Handle file-related errors
            print("Error: Unable to save teams to file.", e)

    # Function to restore the .txt file from your directory to this program
    def restore_teams_from_file(self):
         # Clear the existing team list before restoring from file
        self.team_list.clear()
        # Get the directory path of the current Python script
        folder_path = os.path.dirname(os.path.abspath(__file__))
        # Prompt the user to enter the name of the file to restore
        file_name = input("Enter the name of the file you want to restore: ")
        # Append the file extension .txt if not provided by the user
        file_name += ".txt"
        # Construct the full file path by joining the folder path and file name
        file_path = os.path.join(folder_path, file_name)       
        try:
            # Open the file in read mode
            with open(file_path, 'r') as file:
                # Read all lines from the file
                lines = file.readlines()
                # Skip the header line
                for line in lines[1:]:
                    # Remove leading and trailing whitespace from the line
                    line = line.strip()
                    # Check if the line is not empty
                    if line:
                        # Split the line into fields using comma as delimiter
                        fields = line.split(',')
                        # Extract values from the fields
                        team_id = int(fields[0])
                        date_created = fields[1]
                        name = fields[2]
                        team_type = fields[3]
                        payment_status = fields[4]
                        amount_to_be_paid = int(fields[5])
                        cancellation_date = fields[6] if len(fields) > 6 else None
                        # Create a Team object with the extracted values
                        object_team = Team(name, team_type, payment_status, amount_to_be_paid, date_created)
                        # Set cancellation date if available
                        if cancellation_date:
                            object_team.set_cancellation_date(cancellation_date)
                        # Set the team ID directly without incrementing the ID counter
                        object_team._Team__id = team_id
                        # Add the team to the team list
                        self.team_list.append(object_team)
            # Print success message
            print("Teams information restored successfully.")
        except IOError as e:
            # Handle file-related errors
            print("Error: Unable to restore teams from file.", e)

    















