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


def update_employee_calendar(employees, date, shift_hours, best_individual):
    # Maps each employee index to the hours they work
    employee_assignments = dict()

    for hour, employee_index in zip(shift_hours, best_individual):
        if employee_index not in employee_assignments:
            employee_assignments[employee_index] = []
        employee_assignments[employee_index].append(hour)

    for employee_index, hours in employee_assignments.items():
        # Find the corresponding employee by their index
        employee = next((emp for emp in employees if emp.index == employee_index), None)
        if employee:
            for hour in hours:
                if date not in employee.personal_calendar:
                    employee.personal_calendar[date] = {}
                employee.personal_calendar[date][hour] = "Work"


def update_schedule_with_names(date, shift_num, best_individual, employees, schedule):
    # Assuming each employee in 'employees' list has an 'index' and 'name' attribute
    index_to_name = {emp.index: emp.name for emp in employees}  # Create an index-to-name mapping

    # Retrieve shift hours for the current shift
    shift_hours = schedule[date][shift_num]

    # Update shift_hours with employee names instead of "Empty" or any placeholder
    for hour_index, employee_index in enumerate(best_individual):
        # Assuming shift_hours is a list of hour keys (e.g., [10, 11, 12, ...])
        hour = list(shift_hours.keys())[hour_index]
        employee_name = index_to_name.get(employee_index, "Unknown")  # Safely get the employee name
        shift_hours[hour] = employee_name  # Update the schedule

    # Now, schedule_copy is updated in-place; no need to return it explicitly

