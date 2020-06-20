from ExerciseOptions import Exercises
import random


class Exercise:

    def __init__(self, exercise):
        self.exercise = exercise
        self.intensity = None
        self.RPE = 0
        self.RIR = 7
        self.sets = 3
        self.Reps = []
        self.Volume = 0
        self.Week = 1

    def __str__(self):
        """Returns string format of node."""
        return '(' + str(self.exercise) + ', Weight: ' + str(self.intensity) + ', Sets: ' + str(
            self.sets) + ', RIR: ' + str(self.RIR) + ', Volume: ' + str(self.Volume) + ', RPE: ' + str(
            self.RPE) + ', Week: ' + str(self.Week) + ')'

    __repr__ = __str__


class Days(Exercises):

    def __init__(self):
        super().__init__()
        self._week = {"day1": [], "day2": [], "day3": [], "day4": []}

    def generate_workout(self):
        self._week["day1"].append(Exercise(random.choice(self._quadsPrim)))
        self._week["day1"].append(Exercise(random.choice(self._HorzPrim)))
        self._week["day1"].append(Exercise(random.choice(self._PostPrim)))
        self._week["day1"].append(Exercise(random.choice(self._VertPull)))
        self._week["day1"].append(Exercise(random.choice(self._biceps)))
        self._week["day1"].append(Exercise(random.choice(self._Core)))
        self._week["day2"].append(Exercise(random.choice(self._quadsPrim)))
        self._week["day2"].append(Exercise(random.choice(self._HorzPrim)))
        self._week["day2"].append(Exercise(random.choice(self._PostSupp)))
        self._week["day2"].append(Exercise(random.choice(self._HorzPull)))
        self._week["day2"].append(Exercise(random.choice(self._TricepSupp)))
        self._week["day2"].append(Exercise(random.choice(self._Core)))
        self._week["day3"].append(Exercise(random.choice(self._HorzPrim)))
        self._week["day3"].append(Exercise(random.choice(self._HorzPullSupp)))
        self._week["day3"].append(Exercise(random.choice(self._HorzPull)))
        self._week["day3"].append(Exercise(random.choice(self._TricepPrim)))
        self._week["day3"].append(Exercise(random.choice(self._shouldersSupp)))
        self._week["day3"].append(Exercise(random.choice(self._biceps)))
        self._week["day3"].append(Exercise(random.choice(self._TricepSupp)))
        self._week["day4"].append(Exercise(random.choice(self._quadsPrim)))
        self._week["day4"].append(Exercise(random.choice(self._PostPrim)))
        self._week["day4"].append(Exercise(random.choice(self._SingleLeg)))
        self._week["day4"].append(Exercise(random.choice(self._QuadSupp)))
        self._week["day4"].append(Exercise(random.choice(self._Core)))
        return

    def starting_weight(self):
        for days in self._week:
            for ex in self._week[days]:
                if ex.exercise in self._HorzPrim or ex.exercise in self._VertPull or ex.exercise in self._HorzPull or ex.exercise in self._VertPush or ex.exercise in self._TricepPrim or ex.exercise in self._quadsPrim or ex.exercise in self._PostPrim:
                    weight = int(input("Enter 12 RM for " + ex.exercise + ": "))
                    weight = weight * 0.90
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight
                else:
                    weight = int(input("Enter 15 RM for " + ex.exercise + ": "))
                    weight = weight * 0.90
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight

    def daily_update(self, day):
        for days in self._week:
            if days == day:
                for work in self._week[days]:
                    for reps in range(1, work.sets + 1):
                        work.Reps.append(
                            int(input("Number of reps performed for set " + str(reps) + " of " + work.exercise + ": ")))
                    work.RPE = int(input("Enter RPE experienced on last set on a scale of 0-4: "))
                return

    def weekly_update(self):
        for days in self._week:
            for ex in self._week[days]:
                if ex.Week == 1 or ex.Week == 3 and ex.RIR < 3:
                    ex.sets += 1
                    ex.RIR += 1
                    weight = ex.intensity * 1.05
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight
                    ex.Week += 1
                    continue
                if ex.Week == 1 or ex.Week == 3 and ex.RIR == 3:
                    ex.Week += 1
                    continue
                if ex.Week == 1 or ex.Week == 3 and ex.RIR == 4:
                    ex.sets -= 1
                    weight = ex.intensity * 0.95
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight
                    ex.Week += 1
                    continue
                if ex.Week == 2 or ex.Week == 4 and ex.RIR < 3:
                    weight = ex.intensity * 1.05
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight
                    ex.Week += 1
                    continue
                if ex.Week == 2 or ex.Week == 4 and ex.RIR == 4:
                    ex.sets -= 1
                    weight = ex.intensity * 0.95
                    weight = weight // 5
                    weight = int(weight * 5)
                    ex.intensity = weight
                    ex.Week += 1
                    continue
                if ex.Week == 2 or ex.Week == 4 and ex.RIR == 3:
                    ex.Week += 1
                    continue
        return


if __name__ == '__main__':
    m = Days()
    m.generate_workout()
    print(m._week["day1"])
    print(m._week["day2"])
    print(m._week["day3"])
    print(m._week["day4"])
    m.starting_weight()
    print(m._week["day1"])
    print(m._week["day2"])
    print(m._week["day3"])
    print(m._week["day4"])
    m.daily_update("day1")
    m.weekly_update()
    print(m._week)
