# Define the class information, including scaling factor and minimum attendance percentage
# 'Module name': {'total_hours': 60, 'scaling_factor': 1, 'min_attendance_percent': 75},
# scale factor default: 1.0
# scale factor is for how much hours you clock in each time you attend yoru classes. e.g. 1 physical hour you attend class is 1hr marked in your record

classes = {
    'Class 1': {'total_hours': 60, 'scaling_factor': 1.0, 'min_attendance_percent': 75},
    'Class 2': {'total_hours': 60, 'scaling_factor': 1.0, 'min_attendance_percent': 75},
}

def calculate_max_missable_hours(total_hours, attended_percentage, scaling_factor, min_attendance_percent):
    # Calculate the physical class hours based on the scaling factor
    physical_class_hours = total_hours / scaling_factor

    # Calculate the minimum attendance hours required in the real-world scale
    required_attendance_hours = (min_attendance_percent / 100) * physical_class_hours

    # Calculate the total attended hours based on the attended percentage in real-world terms
    attended_hours = (attended_percentage / 100) * physical_class_hours

    # Calculate the maximum hours that can be missed in real-world terms
    max_missed_hours = attended_hours - required_attendance_hours

    # Ensure we do not return negative missed hours
    return max(max_missed_hours, 0)

def get_class_selection():
    """Handles class selection input from the user"""
    print("Select a module by number:")
    for index, class_name in enumerate(classes.keys(), 1):
        print(f"{index}. {class_name}")
    print("Type 'exit' to quit.")

    user_input = input("Enter the number corresponding to the module: ")

    if user_input.lower() == 'exit':
        return None  # Exit the program

    try:
        selected_index = int(user_input)
        if 1 <= selected_index <= len(classes):
            return list(classes.keys())[selected_index - 1]
        else:
            print("Invalid selection! Please choose a valid number.\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

    return None  # In case of invalid selection

def get_attendance_percentage(selected_class):
    """Handles attendance percentage input from the user"""
    while True:
        user_input = input(f"Enter attendance percentage for {selected_class} (0-100%) or type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            return None  # Exit the program

        try:
            attended_percentage = float(user_input)
            if 0 <= attended_percentage <= 100:
                return attended_percentage
            else:
                print("Invalid percentage! Please enter a value between 0 and 100.\n")
        except ValueError:
            print("Invalid input! Please enter a numeric value between 0 and 100.\n")

def main():
    print("Welcome to 'MissedIt Buddy'!\n")

    while True:
        selected_class = get_class_selection()
        if selected_class is None:
            print("Exiting the program. Goodbye!")
            return

        attended_percentage = get_attendance_percentage(selected_class)
        if attended_percentage is None:
            print("Exiting the program. Goodbye!")
            return

        # Retrieve class info from the dictionary
        class_info = classes[selected_class]
        total_hours = class_info['total_hours']
        scaling_factor = class_info['scaling_factor']
        min_attendance_percent = class_info['min_attendance_percent']

        # Calculate maximum missed hours
        max_missed_hours = calculate_max_missable_hours(total_hours, attended_percentage, scaling_factor,
                                                        min_attendance_percent)

        if max_missed_hours == 0:
            print(f"\nYou cannot miss any more hours for {selected_class}. Your attendance is at or below the required {min_attendance_percent}%.\n")
        else:
            print(f"\nYou can miss {max_missed_hours:.2f} real-world hours for {selected_class}.\n")

        print("-" * 40)  # Separator line for better formatting

if __name__ == "__main__":
    main()
