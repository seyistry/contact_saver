from pathlib import Path
from participant_pkg.file_ops import save_participant, load_participants

CSV_PATH = Path('contacts.csv')


def get_valid_input(prompt, validate_func, error_msg):
    while True:
        value = input(prompt)
        if validate_func(value):
            return value
        print(f"Error: {error_msg}\n")


def is_valid_name(name):
    return bool(name.strip())


def is_valid_age(age):
    try:
        age_int = int(age)
        return age_int > 0
    except ValueError:
        return False


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11


def is_valid_track(track):
    return bool(track.strip())


def main():
    print("\nWelcome to Contact Saver!\n")
    while True:
        name = get_valid_input(
            "Enter Name:\t", is_valid_name, "Name must not be empty.")
        age = get_valid_input("Enter Age:\t", is_valid_age,
                              "Age must be a positive integer.")
        phone = get_valid_input(
            "Enter Phone (11 digits):\t", is_valid_phone, "Phone must be 11 digits.")
        track = get_valid_input(
            "Enter Track:\t", is_valid_track, "Track must not be empty.")

        participant = {
            'Name': name.strip(),
            'Age': int(age),
            'Phone': phone.strip(),
            'Track': track.strip()
        }

        try:
            save_participant(CSV_PATH, participant)
            print("Participant saved successfully!\n")
        except Exception as e:
            print(f"Failed to save participant: {e}\n")

        more = input("Add another participant? (y/n): ").lower()
        if more != 'y':
            break

    try:
        participants = load_participants(CSV_PATH)
        print(f"\nSummary: {len(participants)} participant(s) saved.")
        for p in participants:
            print(f"- {p['Name']} ({p['Age']}), {p['Phone']}, {p['Track']}")
    except Exception as e:
        print(f"Failed to load participants: {e}")


if __name__ == "__main__":
    main()
