import random


class Exercises:

    def __init__(self):
        self._chestPrim = ("Flat Bench", "Incline Bench", "Decline Bench", "Swiss Bar Bench", "DB Flat", "DB Incline",
                           "Machine Chest Press", "Dips Fwd Lean")
        self._chestSupp = (
            "Flat Fly", "Incline Fly", "High Cable Crossover", "Low Cable Crossover", "Push Up Variation")
        self._lats = (
            "Pull Ups", "Chin Ups", "Pullover", "DB Row to hip", "Bent Over Row", "Underhand Pulldown", "Lat Pulldown",
            "Neutral Grip Pulldown", "Single Arm Pulldown", "Machine Row")
        self._upper_back = (
            "Chest Supported Row", "Seated Cable Row", "Face Pull", "Machine Row", "Meadow's Row", "Inverted Row",
            "DB Row to Chest")
        self._shouldersPrim = (
            "Arnold Press", "Overhead Press", "DB Military Press", "High Incline Press", "Machine Shoulder Press")
        self._shouldersSupp = (
            "Band Pull Apart", "Lateral Raises", "Iso-Laterals", "Face Pull", "Hang Clean", "L Raise", "Reverse Fly",
            "Blackburns", "3 Way Raise")
        self._biceps = (
            "Spider Curls", "DB Curls", "Barbell Curl", "Zottman Curl", "Hammer Curl", "Cable Curl", "Preacher Curl",
            "Incline Curl", "EZ Curl")
        self._triceps = (
            "Floor Press", "Close Grip Incline", "JM Press", "Close Grip Bench", "Upright Dips", "V-Handle Pushdown",
            "Straight Bar Pushdown", "Rope Pushdown", "Cable Overhead Ext.", "Skullcrusher", "DB Skullcrusher",
            "Rolling Tricep Ext.")
        self._quadsPrim = (
            "Box Squats", "Front Squat", "Hack Squat", "Leg Press", "Safety Bar Squat", "High Bar Squat",
            "Low Bar Squat")
        self._quadAssc = ("Lunges", "Leg Ext.", "Bulgarian Split Squat")
        self._posterior_chainPrime = ("GHR", "RDL", "Snatch Grip RDL", "DB RDL", "Hip Thrust", "Good Morning")
        self._posterior_chainSupp = (
            "Seated Leg Curl", "Lying Leg Curl", "Single Leg Curl", "Single Leg RDL", "Reverse Lunge")
        self._calves = ("Leg Press Calf Raise", "Seated Calf Raise", "Standing Calf Raise")


class FullBody(Exercises):

    def __init__(self, days):
        super().__init__()
        self._days = days
        self._workout_A = {}
        self._workout_B = {}
        self._workout_C = {}

    def create_workout(self):
        if self._days == 3:
            self._workout_A.update({random.choice(self._quadsPrim): "4 x 6", random.choice(self._chestPrim): "4 x 6",
                                    random.choice(self._lats): "3 x 8", random.choice(self._biceps): "3 x 12",
                                    random.choice(self._triceps): "3 x 15"})
            self._workout_B.update(
                {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._shouldersPrim): "4 x 6",
                 random.choice(self._upper_back): "3 x 8", random.choice(self._chestSupp): "3 x 12",
                 random.choice(self._biceps): "3 x 15"})
            self._workout_C.update({random.choice(self._chestPrim): "3 x 8", random.choice(self._upper_back): "3 x 8",
                                    random.choice(self._quadAssc): "3 x 12",
                                    random.choice(self._posterior_chainSupp): "3 x 12",
                                    random.choice(self._shouldersSupp): "3 x 15"})
            return
        elif self._days == 2:
            self._workout_A.update({random.choice(self._quadsPrim): "4 x 6", random.choice(self._chestPrim): "4 x 6",
                                    random.choice(self._lats): "3 x 8", random.choice(self._shouldersSupp): "3 x 12",
                                    random.choice(self._triceps): "3 x 15"})
            self._workout_B.update(
                {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._shouldersPrim): "4 x 6",
                 random.choice(self._upper_back): "3 x 8", random.choice(self._chestSupp): "3 x 12",
                 random.choice(self._biceps): "3 x 15"})
            return

    def get_workout(self):
        if self._days == 2:
            print(self._workout_A)
            print(self._workout_B)
            return self._workout_A, self._workout_B
        elif self._days == 3:
            print(self._workout_A)
            print(self._workout_B)
            print(self._workout_C)
            return self._workout_A, self._workout_B, self._workout_C


class UpperLower(Exercises):

    def __init__(self):
        super().__init__()
        self._upperA = {}
        self._lowerA = {}
        self._upperB = {}
        self._lowerB = {}

    def create_workout(self):
        self._upperA.update({random.choice(self._chestPrim): "4 x 6", random.choice(self._upper_back): "4 x 8",
                             random.choice(self._chestSupp): "3 x 12", random.choice(self._shouldersSupp): "3 x 15",
                             random.choice(self._biceps): "3 x 12", random.choice(self._triceps): "3 x 15"})
        self._lowerA.update(
            {random.choice(self._quadsPrim): "4 x 6", random.choice(self._posterior_chainPrime): "4 x 8",
             random.choice(self._quadAssc): "3 x 12", random.choice(self._posterior_chainSupp): "3 x 15",
             random.choice(self._calves): "3 x 15"})
        self._upperB.update({random.choice(self._shouldersPrim): "4 x 8", random.choice(self._lats): "4 x 8",
                             random.choice(self._chestPrim): "3 x 10", random.choice(self._upper_back): "3 x 12",
                             random.choice(self._biceps): "3 x 15", random.choice(self._triceps): "3 x 12"})
        self._lowerB.update(
            {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._quadsPrim): "4 x 8",
             random.choice(self._posterior_chainPrime): "3 x 12", random.choice(self._quadAssc): "3 x 15",
             random.choice(self._calves): "3 x 15"})
        return

    def get_workout(self):
        print(self._upperA)
        print(self._lowerA)
        print(self._upperB)
        print(self._lowerB)
        return self._upperA, self._lowerA, self._upperB, self._lowerB


class PPL(Exercises):
    def __init__(self):
        super().__init__()
        self._pushA = {}
        self._pullA = {}
        self._legsA = {}
        self._pushB = {}
        self._pullB = {}
        self._legsB = {}

    def create_workout(self):
        self._pushA.update(
            {random.choice(self._chestPrim): "4 x 8", random.choice(self._chestSupp): "3 x 15",
             random.choice(self._shouldersPrim): "4 x 10", random.choice(self._triceps): "3 x 15"})
        self._pullA.update(
            {random.choice(self._lats): "4 x 12", random.choice(self._upper_back): "4 x 8",
             random.choice(self._lats): "3 x 15", random.choice(self._biceps): "3 x 12"})
        self._legsA.update(
            {random.choice(self._quadsPrim): "4 x 12", random.choice(self._posterior_chainPrime): "4 x 12",
             random.choice(self._quadAssc): "3 x 15", random.choice(self._calves): "3 x 15"})
        self._pushB.update(
            {random.choice(self._shouldersPrim): "4 x 10", random.choice(self._shouldersSupp): "3 x 15",
             random.choice(self._chestPrim): "4 x 8", random.choice(self._triceps): "4 x 12"})
        self._pullB.update(
            {random.choice(self._upper_back): "4 x 12", random.choice(self._lats): "4 x 10",
             random.choice(self._upper_back): "3 x 15", random.choice(self._biceps): "4 x 15"})
        self._legsB.update(
            {random.choice(self._posterior_chainPrime): "4 x 12", random.choice(self._quadsPrim): "4 x 12",
             random.choice(self._posterior_chainSupp): "3 x 15", random.choice(self._calves): "3 x 15"})
        return

    def get_workout(self):
        print(self._pushA)
        print(self._pullA)
        print(self._legsA)
        print(self._pushB)
        print(self._pullB)
        print(self._legsB)
        return self._pushA, self._pullA, self._legsA, self._pushB, self._pullB, self._legsB


class PHAT(Exercises):

    def __init__(self):
        super().__init__()
        self._push = {}
        self._legs = {}
        self._pull = {}
        self._lower = {}
        self._upper = {}

    def create_workout(self):
        self._push.update(
            {random.choice(self._chestPrim): "4 x 8", random.choice(self._chestSupp): "3 x 15",
             random.choice(self._shouldersPrim): "4 x 10", random.choice(self._triceps): "3 x 15"})
        self._legs.update(
            {random.choice(self._quadsPrim): "4 x 12", random.choice(self._posterior_chainPrime): "4 x 12",
             random.choice(self._quadAssc): "3 x 15", random.choice(self._calves): "3 x 15"})
        self._pull.update(
            {random.choice(self._upper_back): "4 x 12", random.choice(self._lats): "4 x 10",
             random.choice(self._upper_back): "3 x 15", random.choice(self._biceps): "3 x 12"})
        self._lower.update(
            {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._quadsPrim): "4 x 8",
             random.choice(self._posterior_chainPrime): "3 x 12", random.choice(self._quadAssc): "3 x 15",
             random.choice(self._calves): "3 x 15"})
        self._upper.update(
            {random.choice(self._shouldersPrim): "4 x 8", random.choice(self._lats): "4 x 8",
             random.choice(self._chestPrim): "3 x 10", random.choice(self._upper_back): "3 x 12",
             random.choice(self._biceps): "3 x 15", random.choice(self._triceps): "3 x 12"})
        return

    def get_workout(self):
        print(self._push)
        print(self._legs)
        print(self._pull)
        print(self._lower)
        print(self._upper)
        return self._push, self._legs, self._pull, self._lower, self._upper
