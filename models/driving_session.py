"""
Driving Session Class
Stores a driver's monitoring session.
"""


class DrivingSession:
    """Represents one driving session."""

    def __init__(self, driver_id, date, posture,
                 sitting_duration, sleep_hours,
                 stress_level, heart_rate,
                 fatigue_level, safety_score):

        self._driver_id = driver_id
        self._date = date
        self._posture = posture
        self._sitting_duration = sitting_duration
        self._sleep_hours = sleep_hours
        self._stress_level = stress_level
        self._heart_rate = heart_rate
        self._fatigue_level = fatigue_level
        self._safety_score = safety_score

    # ---------- Getters ----------

    def get_driver_id(self):
        return self._driver_id

    def get_date(self):
        return self._date

    def get_posture(self):
        return self._posture

    def get_sitting_duration(self):
        return self._sitting_duration

    def get_sleep_hours(self):
        return self._sleep_hours

    def get_stress_level(self):
        return self._stress_level

    def get_heart_rate(self):
        return self._heart_rate

    def get_fatigue_level(self):
        return self._fatigue_level

    def get_safety_score(self):
        return self._safety_score

    # ---------- Display ----------

    def display_session(self):
        """Display one monitoring session."""

        print("\n========== DRIVING SESSION ==========")
        print(f"Driver ID         : {self._driver_id}")
        print(f"Date              : {self._date}")
        print(f"Posture           : {self._posture}")
        print(f"Sitting Duration  : {self._sitting_duration} minutes")
        print(f"Sleep Hours       : {self._sleep_hours}")
        print(f"Stress Level      : {self._stress_level}")
        print(f"Heart Rate        : {self._heart_rate} bpm")
        print(f"Fatigue Level     : {self._fatigue_level}")
        print(f"Safety Score      : {self._safety_score}")