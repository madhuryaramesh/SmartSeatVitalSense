"""
User Class
Parent class for Admin and Driver.
"""


class User:
    """Base class for all users."""

    def __init__(self, user_id, name, username, password):
        self._user_id = user_id
        self._name = name
        self._username = username
        self._password = password

    # ---------- Getters ----------

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    # ---------- Setters ----------

    def set_name(self, name):
        self._name = name

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    # ---------- Display ----------

    def display_user(self):
        print("\n========== USER DETAILS ==========")
        print(f"User ID  : {self._user_id}")
        print(f"Name     : {self._name}")
        print(f"Username : {self._username}")