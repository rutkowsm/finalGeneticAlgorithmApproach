class Employee:
    def __init__(self, name, index, min_shift_lenght=0, max_shift_lenght=16,
                 min_weekly_hours=0, max_weekly_hours=100, personal_calendar=None):
        self.name = name
        self.index = index
        self.min_shift_lenght = min_shift_lenght
        self.max_shift_lenght = max_shift_lenght
        self.min_weekly_hours = min_weekly_hours
        self.max_weekly_hours = max_weekly_hours
        self.personal_calendar = personal_calendar
