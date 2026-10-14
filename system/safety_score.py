"""
Safety Score Module
Calculates driver's safety score.
"""


class SafetyScore:

    @staticmethod
    def calculate_score(seat):
        """
        Calculate safety score based on
        SmartSeat monitoring data.
        """

        score = 100

        # Poor posture
        if seat.get_posture() == "Poor":
            score -= 15

        # Long sitting duration
        if seat.get_sitting_duration() > 120:
            score -= 15

        # Low sleep
        if seat.get_sleep_hours() < 6:
            score -= 20

        # High stress
        if seat.get_stress_level() == "High":
            score -= 15
        elif seat.get_stress_level() == "Medium":
            score -= 5

        # High heart rate
        if seat.get_heart_rate() > 100:
            score -= 15
        elif seat.get_heart_rate() > 90:
            score -= 5

        # Fatigue level
        if seat.get_fatigue_level() == "High":
            score -= 20
        elif seat.get_fatigue_level() == "Medium":
            score -= 10

        # Prevent negative scores
        if score < 0:
            score = 0

        return score

    @staticmethod
    def get_safety_status(score):
        """
        Return safety status based on score.
        """

        if score >= 90:
            return "Excellent"

        elif score >= 75:
            return "Good"

        elif score >= 60:
            return "Average"

        elif score >= 40:
            return "Risky"

        else:
            return "Critical"