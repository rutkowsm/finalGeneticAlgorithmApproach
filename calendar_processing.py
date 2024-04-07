import data
import employee as e


def calculate_lenght_of_shift(shift):
    return len(shift)


def process_employees(employees):
    employee_list = [
        e.Employee(
            name=name,
            index=index + 1,
            min_shift_lenght=info.get('min_shift_len', 0),
            max_shift_lenght=info.get('max_shift_len', 16),
            personal_calendar=info.get('calendar', None),
        )
        for index, (name, info) in enumerate(employees.items())
    ]
    return employee_list


def process_shift_unavailabilities(employees, day, shift_num, shift_hours):
    """
    Process unavailabilities for a single shift.

    Args:
        employees (list): List of Employee instances.
        day (str): The day of the shift.
        shift_num (int): The shift number.
        shift_hours (dict): The shift hours.

    Returns:
        dict: Unavailabilities for the given shift.
    """
    # Initialize storage for this shift's unavailability
    shift_unavailabilities = {}

    # Calculate the shift length
    sorted_shift_hours = sorted(shift_hours)
    shift_length = len(sorted_shift_hours)

    for employee in employees:
        # Check if there's a matching day in the employee's calendar
        emp_day_schedule = employee.personal_calendar.get(day, {})

        # Collect indexes of busy hours within this shift
        busy_hour_indexes = [sorted_shift_hours.index(hour) for hour, status in emp_day_schedule.items()
                             if hour in sorted_shift_hours and status != "Empty"]

        if busy_hour_indexes:
            # Record the employee's unavailable indexes for this shift
            shift_unavailabilities[employee.index] = busy_hour_indexes

    return {
        "shift_len": shift_length,
        "unavailabilities": shift_unavailabilities
    }


def update_employee_calendar(date, shift_hours, best_individual, employees):
    """
    Correctly update the personal calendar of each employee assigned to a shift,
    marking them as busy for the hours of that shift.

    Args:
        date (str): The day of the shift.
        shift_hours (list): List of integers representing the hours of the shift.
        best_individual (list of int): List of employee indexes (adjusted for zero-based indexing) assigned to the shift.
        employees (list of Employee): List of Employee instances.
    """
    for employee_index in best_individual:  # Assuming these are already adjusted for zero-based indexing
        # Find the employee by index
        employee = next((e for e in employees if e.index == employee_index), None)
        if employee:
            # Ensure the day exists in the employee's personal calendar
            if date not in employee.personal_calendar:
                employee.personal_calendar[date] = {}
            for hour in shift_hours:
                # Mark each hour of the shift as "Busy"
                employee.personal_calendar[date][hour] = "Work"


def update_shift_with_employee_names(schedule, date, shift_num, employee_indexes, index_to_employee_name):
    shift_hours = schedule[date][shift_num]

    for i, hour in enumerate(sorted(shift_hours.keys())):
        employee_index = employee_indexes[i]  # Now directly using the integer index
        employee_name = index_to_employee_name[employee_index]
        shift_hours[hour] = employee_name



