class Exercises:
    """Represents collection of exercises labeled by movement pattern."""

    def __init__(self):
        self._HorzPrim = (
            "Flat Bench", "Incline Bench", "Decline Bench", "Swiss Bar Bench", "DB Flat", "DB Incline",
            "Machine Chest Press", "One Arm Flat DB", "One Arm Incline DB")  # Primary exercises for chest.
        self._ChestIso = (
            "Flat Fly", "Incline Fly", "Decline Fly", "High Cable Crossover", "Mid-Level Cable Crossover", "Low Cable Crossover")
        self._VertPull = (
            "Pull Ups", "Chin Ups", "Underhand Pulldown", "Lat Pulldown",
            "Neutral Grip Pulldown", "Single Arm Pulldown", "High Row")  # Exercises for lats.
        self._HorzPull = (
            "Chest Supported Row", "Seated Cable Row", "Machine Row", "Meadow's Row", "Bent Over Row",
            "DB Row", "Pendlay Row")  # Exercises for upper back (middle traps, rhomboids, rear deltoids).
        self._VertPush = (
            "Arnold Press", "Z Press", "Standing DB Press", "High Incline Press", "Machine Shoulder Press",
            "Seated OHP", "Unsupported Seated OHP")
        # Primary exercises for shoulders.
        self._shouldersSupp = (
            "Lateral Raises", "Iso-Laterals", "L Raise", "3 Way Raise")  # Secondary exercises for shoulders.
        self._HorzPullSupp = (
            "Band Apart", "Reverse Fly", "Pullover", "Shrugs", "T Raise", "Y Raise", "W Raise", "Blackburn")
        self._biceps = (
            "DB Curls", "Fat Grip Barbell Curl", "Hammer Curl", "Cable Curl", "Incline Curl", "EZ Curl")
        # Exercises for biceps.
        self._TricepPrim = (
            "Floor Press", "Rack Press", "Dips", "JM Press", "Close Grip Incline", "Close Grip Bench")
        self._TricepSupp = (
            "V-Handle Pushdown",
            "Straight Bar Pushdown", "Rope Pushdown", "Cable Overhead Ext.", "Skullcrusher", "DB Skullcrusher",
            "Rolling Tricep Ext.")  # Exercises for triceps.
        self._quadsPrim = (
            "Box Squats", "Front Squat", "Hack Squat", "Leg Press", "Safety Bar Squat", "High Bar Squat",
            "Low Bar Squat")  # Primary quadriceps exercises.
        self._QuadSupp = (
            "Leg Ext.", "Single Leg Ext.")  # Secondary quadriceps exercises.
        self._PostPrim = (
            "RDL", "Snatch Grip RDL", "DB RDL", "Good Morning")
        # Primary posterior chain (hamstring, glutes) exercises.
        self._Core = (
            "Ab Wheel", "Cable Crunch", "Sit & Reach")
        self._PostSupp = (
            "GHR", "Seated Leg Curl", "Lying Leg Curl", "Single Leg Curl", "Single Leg RDL", "Reverse Lunge")
        # Secondary posterior chain (hamstring, glutes) exercises.
        self._SingleLeg = (
            "Reverse Lunge", "Zercher Reverse Lunge", "Single Leg RDL", "Bulgarian Split Squat", "Step Ups",
            "Hatfield Skater Squats")
        self._calves = (
            "Leg Press Calf Raise", "Seated Calf Raise", "Standing Calf Raise")  # Exercises for calves.

