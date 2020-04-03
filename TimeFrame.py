import WorkoutGenerator

class Calendar:

    def __init__(self, name, weeks):
        self._name = name
        self._length = weeks * 7
        self._calendar = {}
        for days in range(1, weeks + 1):
            for cycles in range(1, 8):
                self._calendar[days, cycles] = 0

    def get_calendar(self):
        print(self._calendar)
        return self._calendar


Time = Calendar("Chris", 6)
Time.get_calendar()

