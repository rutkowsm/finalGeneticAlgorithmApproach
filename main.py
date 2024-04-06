import employee as e
import data as d

current_schedule = d.schedule
current_employees = d.employees

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


def process_employee_shift_unavailabilities(employees, schedule):
    employee_shift_unavailabilities = {}

    for day, shifts in schedule.items():
        # Ensure there's an entry for the day
        if day not in employee_shift_unavailabilities:
            employee_shift_unavailabilities[day] = {}

        for shift_num, shift_hours in shifts.items():
            # Prepare a list of the shift hours to calculate indexes
            sorted_shift_hours = sorted([int(hour) for hour in shift_hours.keys()])
            shift_start = sorted_shift_hours[0]

            # Initialize storage for this shift's unavailability
            shift_unavailabilities = {}

            for employee in employees:
                # Check if there's a matching day in the employee's calendar
                emp_day_schedule = employee.personal_calendar.get(day, {})

                # Collect indexes of busy hours within this shift
                busy_hour_indexes = [sorted_shift_hours.index(int(hour)) for hour, status in emp_day_schedule.items() if
                                     status == "Busy" and int(hour) in sorted_shift_hours]

                if busy_hour_indexes:
                    # Record the employee's unavailable indexes for this shift
                    shift_unavailabilities[employee.index] = busy_hour_indexes

            # If there are any unavailabilities found, add them under the current shift
            if shift_unavailabilities:
                employee_shift_unavailabilities[day][shift_num] = shift_unavailabilities

    return employee_shift_unavailabilities


print(process_employee_shift_unavailabilities(process_employees(current_employees), current_schedule))







