import json

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

def filter_users_by_age(min_age=None, max_age=None):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = users
    if min_age is not None:
        filtered_users = [user for user in filtered_users if user["age"] >= min_age]
    if max_age is not None:
        filtered_users = [user for user in filtered_users if user["age"] <= max_age]
    
    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        min_age_input = input("Enter minimum age (or leave blank): ").strip()
        max_age_input = input("Enter maximum age (or leave blank): ").strip()
        
        min_age = int(min_age_input) if min_age_input else None
        max_age = int(max_age_input) if max_age_input else None
        
        filter_users_by_age(min_age, max_age)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
