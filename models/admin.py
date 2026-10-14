"""
Administrator Class
Inherits from the User class.
"""

from models.user import User


class Admin(User):
    """Administrator class."""

    def __init__(self, user_id, name, username, password):
        super().__init__(user_id, name, username, password)

    def display_profile(self):
        """Display administrator profile."""

        print("\n========== ADMIN PROFILE ==========")
        print(f"Admin ID : {self.get_user_id()}")
        print(f"Name     : {self.get_name()}")
        print(f"Username : {self.get_username()}")
        print("Role     : Administrator")