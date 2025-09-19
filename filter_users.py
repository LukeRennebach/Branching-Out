import json


def load_users():
    """
    Load users from users.json.
    Returns an empty list if the file is missing or invalid.
    """
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' not found.")
    except json.JSONDecodeError:
        print("Error: 'users.json' is not valid JSON.")
    return []


def filter_users_by_email(email):
    users = load_users()
    if not users:
        return

    # Case-insensitive, tolerate missing keys
    filtered_users = [u for u in users if u.get("email", "").lower() == email.lower()]

    if not filtered_users:
        print("No users found with that email.")
        return

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    users = load_users()
    if not users:
        return

    filtered_users = [u for u in users if u.get("age") == age]

    if not filtered_users:
        print("No users found with that age.")
        return

    for user in filtered_users:
        print(user)


def filter_users_by_name(name):
    users = load_users()
    if not users:
        return

    # Case-insensitive, tolerate missing keys
    filtered_users = [u for u in users if u.get("name", "").lower() == name.lower()]

    if not filtered_users:
        print("No users found with that name.")
        return

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input("What would you like to filter by? (Supported: 'name', 'age', 'email'): ")
        .strip()
        .lower()
    )

    if filter_option == "email":
        email_to_filter = input("What email would you like to filter by?: ").strip()
        filter_users_by_email(email_to_filter)

    elif filter_option == "age":
        raw_age = input("What age would you like to filter by?: ").strip()
        try:
            age_to_filter = int(raw_age)
        except ValueError:
            print("Please enter a valid integer for age.")
        else:
            filter_users_by_age(age_to_filter)

    elif filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    else:
        print("Filtering by that option is not yet supported.")