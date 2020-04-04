import random  # Imports random module.


class Exercises:
    """Represents collection of exercises labeled by bodypart."""

    def __init__(self):
        self._chestPrim = ("Flat Bench", "Incline Bench", "Decline Bench", "Swiss Bar Bench", "DB Flat", "DB Incline",
                           "Machine Chest Press", "Dips Fwd Lean")  # Primary exercises for chest.
        self._chestSupp = (
            "Flat Fly", "Incline Fly", "High Cable Crossover", "Low Cable Crossover", "Push Up Variation")
        # Secondary exercises for chest.
        self._lats = (
            "Pull Ups", "Chin Ups", "Pullover", "DB Row to hip", "Bent Over Row", "Underhand Pulldown", "Lat Pulldown",
            "Neutral Grip Pulldown", "Single Arm Pulldown", "Machine Row")  # Exercises for lats.
        self._upper_back = (
            "Chest Supported Row", "Seated Cable Row", "Face Pull", "Machine Row", "Meadow's Row", "Inverted Row",
            "DB Row to Chest")  # Exercises for upper back (middle traps, rhomboids, rear deltoids).
        self._shouldersPrim = (
            "Arnold Press", "Overhead Press", "DB Military Press", "High Incline Press", "Machine Shoulder Press")
        # Primary exercises for shoulders.
        self._shouldersSupp = (
            "Band Pull Apart", "Lateral Raises", "Iso-Laterals", "Face Pull", "Hang Clean", "L Raise", "Reverse Fly",
            "Blackburns", "3 Way Raise")  # Secondary exercises for shoulders.
        self._biceps = (
            "Spider Curls", "DB Curls", "Barbell Curl", "Zottman Curl", "Hammer Curl", "Cable Curl", "Preacher Curl",
            "Incline Curl", "EZ Curl")  # Exercises for biceps.
        self._triceps = (
            "Floor Press", "Close Grip Incline", "JM Press", "Close Grip Bench", "Upright Dips", "V-Handle Pushdown",
            "Straight Bar Pushdown", "Rope Pushdown", "Cable Overhead Ext.", "Skullcrusher", "DB Skullcrusher",
            "Rolling Tricep Ext.")  # Exercises for triceps.
        self._quadsPrim = (
            "Box Squats", "Front Squat", "Hack Squat", "Leg Press", "Safety Bar Squat", "High Bar Squat",
            "Low Bar Squat")  # Primary quadriceps exercises.
        self._quadAssc = ("Lunges", "Leg Ext.", "Bulgarian Split Squat")  # Secondary quadriceps exercises.
        self._posterior_chainPrime = ("GHR", "RDL", "Snatch Grip RDL", "DB RDL", "Hip Thrust", "Good Morning")
        # Primary posterior chain (hamstring, glutes) exercises.
        self._posterior_chainSupp = (
            "Seated Leg Curl", "Lying Leg Curl", "Single Leg Curl", "Single Leg RDL", "Reverse Lunge")
        # Secondary posterior chain (hamstring, glutes) exercises.
        self._calves = ("Leg Press Calf Raise", "Seated Calf Raise", "Standing Calf Raise")  # Exercises for calves.


class FullBody(Exercises):
    """Represents Full body workout."""

    def __init__(self, days):
        """Initializes Client object with name, workouts, and days available."""
        super().__init__()
        self._days = days  # Initializes number of days client is available each week.
        self._workout_A = {}  # Initializes workout A as an empty dictionary.
        self._workout_B = {}  # Initializes workout B as an empty dictionary.
        self._workout_C = {}  # Initializes workout C as an empty dictionary.

    def create_workout(self):
        """Creates a Full body workout based on number of days available."""
        if self._days >= 3:  # Checks if minimum days available is three.
            self._workout_A.update(
                {random.choice(self._quadsPrim): "4 x 6", random.choice(self._chestPrim): "4 x 6",
                 random.choice(self._lats): "3 x 8", random.choice(self._biceps): "3 x 12",
                 random.choice(self._triceps): "3 x 15"})  # Constructs workout A from Exercise database.
            self._workout_B.update(
                {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._shouldersPrim): "4 x 6",
                 random.choice(self._upper_back): "3 x 8", random.choice(self._chestSupp): "3 x 12",
                 random.choice(self._biceps): "3 x 15"})  # Constructs workout B from Exercise database.
            self._workout_C.update(
                {random.choice(self._chestPrim): "3 x 8", random.choice(self._upper_back): "3 x 8",
                 random.choice(self._quadAssc): "3 x 12", random.choice(self._posterior_chainSupp): "3 x 12",
                 random.choice(self._shouldersSupp): "3 x 15"})  # Constructs workout C from Exercise database.
            return
        elif self._days <= 2:  # Checks if maximum days available is two.
            self._workout_A.update(
                {random.choice(self._quadsPrim): "4 x 6", random.choice(self._chestPrim): "4 x 6",
                 random.choice(self._lats): "3 x 8", random.choice(self._shouldersSupp): "3 x 12",
                 random.choice(self._triceps): "3 x 15"})  # Constructs workout A from Exercise database.
            self._workout_B.update(
                {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._shouldersPrim): "4 x 6",
                 random.choice(self._upper_back): "3 x 8", random.choice(self._chestSupp): "3 x 12",
                 random.choice(self._biceps): "3 x 15"})  # Constructs workout B from Exercise database.
            return

    def get_workout(self):
        """Retrieves client's workout."""
        if self._days <= 2:  # Checks if maximum available days is two.
            print(self._workout_A)
            print(self._workout_B)
            return self._workout_A, self._workout_B
        elif self._days >= 3:  # Checks if minimum days available is three.
            print(self._workout_A)
            print(self._workout_B)
            print(self._workout_C)
            return self._workout_A, self._workout_B, self._workout_C


class UpperLower(Exercises):
    """Represents Upper Lower exercise program."""

    def __init__(self):
        """Initializes Client object with name and workouts."""
        super().__init__()
        self._upperA = {}  # Initializes upper A workout as empty dictionary.
        self._lowerA = {}  # Initializes lower A workout as empty dictionary.
        self._upperB = {}  # Initializes upper B workout as empty dictionary.
        self._lowerB = {}  # Initializes lower B workout as empty dictionary.

    def create_workout(self):
        """Function that constructs workout for client."""
        self._upperA.update(
            {random.choice(self._chestPrim): "4 x 6", random.choice(self._upper_back): "4 x 8",
             random.choice(self._chestSupp): "3 x 12", random.choice(self._shouldersSupp): "3 x 15",
             random.choice(self._biceps): "3 x 12", random.choice(self._triceps): "3 x 15"})
        # Creates upper A program using exercises from database available.
        self._lowerA.update(
            {random.choice(self._quadsPrim): "4 x 6", random.choice(self._posterior_chainPrime): "4 x 8",
             random.choice(self._quadAssc): "3 x 12", random.choice(self._posterior_chainSupp): "3 x 15",
             random.choice(self._calves): "3 x 15"})
        # Creates lower A program using exercises from database available.
        self._upperB.update(
            {random.choice(self._shouldersPrim): "4 x 8", random.choice(self._lats): "4 x 8",
             random.choice(self._chestPrim): "3 x 10", random.choice(self._upper_back): "3 x 12",
             random.choice(self._biceps): "3 x 15", random.choice(self._triceps): "3 x 12"})
        # Creates upper B program using exercises from database available.
        self._lowerB.update(
            {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._quadsPrim): "4 x 8",
             random.choice(self._posterior_chainPrime): "3 x 12", random.choice(self._quadAssc): "3 x 15",
             random.choice(self._calves): "3 x 15"})
        # Creates lower B program using exercises from database available.
        return

    def get_workout(self):
        """Function to retrieve client's workout."""
        print(self._upperA)
        print(self._lowerA)
        print(self._upperB)
        print(self._lowerB)
        return self._upperA, self._lowerA, self._upperB, self._lowerB


class PPL(Exercises):
    """Represents Push, Pull, Legs, workout."""

    def __init__(self):
        """Initializes Client object with name and workouts."""
        super().__init__()
        self._pushA = {}  # Initializes push A workout as empty dictionary.
        self._pullA = {}  # Initializes pull A workout as empty dictionary.
        self._legsA = {}  # Initializes legs A workout as empty dictionary.
        self._pushB = {}  # Initializes push B workout as empty dictionary.
        self._pullB = {}  # Initializes pull B workout as empty dictionary.
        self._legsB = {}  # Initializes legs B workout as empty dictionary.

    def create_workout(self):
        """Function that creates workout for client."""
        self._pushA.update(
            {random.choice(self._chestPrim): "4 x 8", random.choice(self._chestSupp): "3 x 15",
             random.choice(self._shouldersPrim): "4 x 10", random.choice(self._triceps): "3 x 15"})
        # Creates push A program using exercises from database available.
        self._pullA.update(
            {random.choice(self._lats): "4 x 12", random.choice(self._upper_back): "4 x 8",
             random.choice(self._lats): "3 x 15", random.choice(self._biceps): "3 x 12"})
        # Creates pull A program using exercises from database available.
        self._legsA.update(
            {random.choice(self._quadsPrim): "4 x 12", random.choice(self._posterior_chainPrime): "4 x 12",
             random.choice(self._quadAssc): "3 x 15", random.choice(self._calves): "3 x 15"})
        # Creates legs A program using exercises from database available.
        self._pushB.update(
            {random.choice(self._shouldersPrim): "4 x 10", random.choice(self._shouldersSupp): "3 x 15",
             random.choice(self._chestPrim): "4 x 8", random.choice(self._triceps): "4 x 12"})
        # Creates push B program using exercises from database available.
        self._pullB.update(
            {random.choice(self._upper_back): "4 x 12", random.choice(self._lats): "4 x 10",
             random.choice(self._upper_back): "3 x 15", random.choice(self._biceps): "4 x 15"})
        # Creates pull B program using exercises from database available.
        self._legsB.update(
            {random.choice(self._posterior_chainPrime): "4 x 12", random.choice(self._quadsPrim): "4 x 12",
             random.choice(self._posterior_chainSupp): "3 x 15", random.choice(self._calves): "3 x 15"})
        # Creates legs B program using exercises from database available.
        return

    def get_workout(self):
        """Function to retrieve workout for client."""
        print(self._pushA)
        print(self._pullA)
        print(self._legsA)
        print(self._pushB)
        print(self._pullB)
        print(self._legsB)
        return self._pushA, self._pullA, self._legsA, self._pushB, self._pullB, self._legsB


class PHAT(Exercises):
    """Represents workout program for Power, Hypertrophy, Adaptive Training."""

    def __init__(self):
        """Initializes Client object with name and workouts."""
        super().__init__()
        self._push = {}  # Initializes push workout as empty dictionary.
        self._legs = {}  # Initializes legs workout as empty dictionary.
        self._pull = {}  # Initializes pull workout as empty dictionary.
        self._lower = {}  # Initializes lower workout as empty dictionary.
        self._upper = {}  # Initializes upper workout as empty dictionary.

    def create_workout(self):
        """Function that creates workout for given client."""
        self._push.update(
            {random.choice(self._chestPrim): "4 x 8", random.choice(self._chestSupp): "3 x 15",
             random.choice(self._shouldersPrim): "4 x 10", random.choice(self._triceps): "3 x 15"})
        # Creates push program using exercises from database available.
        self._legs.update(
            {random.choice(self._quadsPrim): "4 x 12", random.choice(self._posterior_chainPrime): "4 x 12",
             random.choice(self._quadAssc): "3 x 15", random.choice(self._calves): "3 x 15"})
        # Creates legs program using exercises from database available.
        self._pull.update(
            {random.choice(self._upper_back): "4 x 12", random.choice(self._lats): "4 x 10",
             random.choice(self._upper_back): "3 x 15", random.choice(self._biceps): "3 x 12"})
        # Creates pull program using exercises from database available.
        self._lower.update(
            {random.choice(self._posterior_chainPrime): "4 x 6", random.choice(self._quadsPrim): "4 x 8",
             random.choice(self._posterior_chainPrime): "3 x 12", random.choice(self._quadAssc): "3 x 15",
             random.choice(self._calves): "3 x 15"})  # Creates lower program using exercises from database available.
        self._upper.update(
            {random.choice(self._shouldersPrim): "4 x 8", random.choice(self._lats): "4 x 8",
             random.choice(self._chestPrim): "3 x 10", random.choice(self._upper_back): "3 x 12",
             random.choice(self._biceps): "3 x 15", random.choice(self._triceps): "3 x 12"})
        # Creates upper program using exercises from database available.
        return

    def get_workout(self):
        """Function that retrieves client's workout."""
        print(self._push)
        print(self._legs)
        print(self._pull)
        print(self._lower)
        print(self._upper)
        return self._push, self._legs, self._pull, self._lower, self._upper
