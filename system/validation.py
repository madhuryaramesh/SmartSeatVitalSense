"""
Validation Module
Provides input validation methods.
"""


class Validation:

    @staticmethod
    def validate_age(age):

        try:
            age = int(age)

            if age < 18 or age > 100:
                return False

            return True

        except ValueError:
            return False

    @staticmethod
    def validate_heart_rate(rate):

        try:
            rate = int(rate)

            if rate < 40 or rate > 200:
                return False

            return True

        except ValueError:
            return False

    @staticmethod
    def validate_sleep(hours):

        try:
            hours = float(hours)

            if hours < 0 or hours > 24:
                return False

            return True

        except ValueError:
            return False

    @staticmethod
    def validate_posture(posture):

        posture = posture.strip().title()

        return posture in ["Good", "Poor"]

    @staticmethod
    def validate_level(level):

        level = level.strip().title()

        return level in ["Low", "Medium", "High"]

    @staticmethod
    def validate_name(name):

        return len(name.strip()) > 0

    @staticmethod
    def validate_username(username):

        return len(username.strip()) >= 4

    @staticmethod
    def validate_password(password):

        return len(password.strip()) >= 4