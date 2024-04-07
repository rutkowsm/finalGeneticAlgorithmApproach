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


def process_employee_shift_unavailabilities(employees, schedule):
    employee_shift_unavailabilities = {}

    for day, shifts in schedule.items():
        employee_shift_unavailabilities[day] = {}

        for shift_num, shift_hours in shifts.items():
            # Calculate the shift length
            sorted_shift_hours = sorted([int(hour) for hour in shift_hours.keys()])
            shift_length = len(sorted_shift_hours)

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

            # Add shift length and unavailabilities for the shift
            employee_shift_unavailabilities[day][shift_num] = {
                "shift_len": shift_length,
                "unavailabilities": shift_unavailabilities
            }

    return employee_shift_unavailabilities