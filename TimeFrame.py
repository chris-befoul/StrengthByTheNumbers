class Calendar:
    """Represents Calendar for intended length of program."""

    def __init__(self, weeks):
        """Initializes calendar with length of program."""
        self._length = weeks * 7  # Initializes length to number of days of program.
        self._calendar = {}  # Initializes calendar as empty dictionary.
        for days in range(1, weeks + 1):  # Loop to iterate through number of weeks.
            for cycles in range(1, 8):  # Loop to iterate through number of days in each week.
                self._calendar[days, cycles] = 0  # Updates calendar to show (week, day) as key in dictionary.

    def get_calendar(self):
        """Retrieves calendar."""
        print(self._calendar)
        return self._calendar


