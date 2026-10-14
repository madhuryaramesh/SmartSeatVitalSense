"""
Smart Seat Class
Stores the driver's seat and health monitoring information.
"""


class SmartSeat:
    """Represents a driver's monitoring data."""

    def __init__(self, posture, sitting_duration, sleep_hours,
                 stress_level, heart_rate, fatigue_level):

        self._posture = posture
        self._sitting_duration = sitting_duration
        self._sleep_hours = sleep_hours
        self._stress_level = stress_level
        self._heart_rate = heart_rate
        self._fatigue_level = fatigue_level

    # ---------- Getters ----------

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

    # ---------- Setters ----------

    def set_posture(self, posture):
        self._posture = posture

    def set_sitting_duration(self, sitting_duration):
        self._sitting_duration = sitting_duration

    def set_sleep_hours(self, sleep_hours):
        self._sleep_hours = sleep_hours

    def set_stress_level(self, stress_level):
        self._stress_level = stress_level

    def set_heart_rate(self, heart_rate):
        self._heart_rate = heart_rate

    def set_fatigue_level(self, fatigue_level):
        self._fatigue_level = fatigue_level

    # ---------- Display ----------

    def display_monitoring(self):
        """Display current monitoring information."""

        print("\n========== SMART SEAT MONITORING ==========")
        print(f"Posture            : {self._posture}")
        print(f"Sitting Duration   : {self._sitting_duration} minutes")
        print(f"Sleep Hours        : {self._sleep_hours}")
        print(f"Stress Level       : {self._stress_level}")
        print(f"Heart Rate         : {self._heart_rate} bpm")
        print(f"Fatigue Level      : {self._fatigue_level}")