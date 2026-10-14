"""
Authentication Module
Handles Admin and Driver login.
"""

from models.admin import Admin
from models.driver import Driver


class Authentication:

    ADMIN_FILE = "data/admins.txt"
    DRIVER_FILE = "data/drivers.txt"

    @staticmethod
    def admin_login():
        """Authenticate an administrator."""

        print("\n========== ADMIN LOGIN ==========")

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        try:
            with open(Authentication.ADMIN_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) != 4:
                        continue

                    admin_id, name, user, pwd = data

                    if username == user and password == pwd:
                        print("\nLogin Successful!\n")

                        return Admin(
                            admin_id,
                            name,
                            user,
                            pwd
                        )

        except FileNotFoundError:
            print("\nAdmin file not found.")

        print("\nInvalid username or password.")
        return None

    @staticmethod
    def driver_login():
        """Authenticate a driver."""

        print("\n========== DRIVER LOGIN ==========")

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        try:
            with open(Authentication.DRIVER_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) != 6:
                        continue

                    driver_id, name, age, license_number, user, pwd = data

                    if username == user and password == pwd:
                        print("\nLogin Successful!\n")

                        return Driver(
                            driver_id,
                            name,
                            int(age),
                            license_number,
                            user,
                            pwd
                        )

        except FileNotFoundError:
            print("\nDriver file not found.")

        print("\nInvalid username or password.")
        return None