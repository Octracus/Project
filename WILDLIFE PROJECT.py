# Initialize an empty dictionary to store wildlife records.
wildlife_data = {}

# Function to add a new wildlife record.
def add_wildlife():
    wildlife_id = input("Enter wildlife ID: ")
    wildlife_name = input("Enter wildlife name: ")
    wildlife_location = input("Enter location of wildlife: ")
    wildlife_species = input("Enter wildlife species: ")
    wildlife_behaviour = input("Enter wildlife behaviour: ")


    wildlife_profile = {
    "wildlife_id": wildlife_id,
    "name_of_wildlife": wildlife_name,
    "location_of_wildlife": wildlife_location,
    "species_of_wildlife": wildlife_species,
    "behaviour_of_wildlife": wildlife_behaviour
}

    wildlife_data[wildlife_id] = wildlife_profile
    print(f"Wildlife data for {wildlife_name} has been added.")



# Function to retrieve a wildlife record by ID.
def retrieve_wildlife_information():
    wildlife_id = input("Enter wildlife ID to retrieve: ")
    if wildlife_id in wildlife_data:
        wildlife = wildlife_data[wildlife_id]
        print("Wildlife Information:")
        print(f"Name: {wildlife['name_of_wildlife']}")
        print(f"Location: {wildlife['location_of_wildlife']}")
        print(f"Species: {wildlife['species_of_wildlife']} ")
        print(f"Wildlife Behaviour: {wildlife['behaviour_of_wildlife']}")
    else:
        print("Wildlife not found.")


# Function to update a wildlife record by ID.
def update_wildlife_information():
    wildlife_id = input("Enter wildlife ID to update: ")
    if wildlife_id in wildlife_data:
        wildlife = wildlife_data[wildlife_id]
        print(f"Updating record for {wildlife['name_of_wildlife']}:")
        wildlife['name_of_wildlife'] = input("Enter new wildlife name: ")
        wildlife['location_of_wildlife'] = (input("Enter new wildlife location: "))
        wildlife['species_of_wildlife'] = (input("Enter new wildlife species: "))
        wildlife['behaviour_of_wildlife'] = (input("Enter new wildlife of behaviour: "))
        print("Updating wildlife information: ")
    else:
        print("Wildlife ID not found.")


def delete_wildlife_information():
# Function to delete wildlife record by ID.
    wildlife_id = input("Enter wildlife ID to delete: ")
    if wildlife_id in wildlife_data:
        wildlife_name = wildlife_data[wildlife_id]['name_of_wildlife']
        del wildlife_data[wildlife_id]
        print(f"Record for {wildlife_name} has been deleted.")
    else:
        print("Wildlife ID not found.")


# Main program loop
while True:
    print("\nWildlife Management System")
    print("1. Add Wildlife Information")
    print("2. Retrieve Wildlife Information")
    print("3. Update Wildlife Information")
    print("4. Delete Wildlife Information")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == '1':
        add_wildlife()
    elif choice == '2':
        retrieve_wildlife_information()
    elif choice == '3':
        update_wildlife_information()
    elif choice == '4':
        delete_wildlife_information()
    elif choice == '5':
        print("Exiting Wildlife Management System. /nGoodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")