"""
Driver Class
Inherits from the User class.
"""

from models.user import User


class Driver(User):
    """Driver class."""

    def __init__(self, user_id, name, age, license_number,
                 username, password):
        super().__init__(user_id, name, username, password)

        self._age = age
        self._license_number = license_number

    # ---------- Getters ----------

    def get_age(self):
        return self._age

    def get_license_number(self):
        return self._license_number

    # ---------- Setters ----------

    def set_age(self, age):
        self._age = age

    def set_license_number(self, license_number):
        self._license_number = license_number

    # ---------- Display ----------

    def display_profile(self):
        """Display driver profile."""

        print("\n========== DRIVER PROFILE ==========")
        print(f"Driver ID      : {self.get_user_id()}")
        print(f"Name           : {self.get_name()}")
        print(f"Age            : {self._age}")
        print(f"License Number : {self._license_number}")
        print(f"Username       : {self.get_username()}")
        print("Role           : Driver")