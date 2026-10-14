"""
Driver Manager Module
Handles all driver management operations.
"""

from system.file_manager import FileManager
from models.driver import Driver


class DriverManager:

    @staticmethod
    def add_driver():

        print("\n========== ADD DRIVER ==========")

        driver_id = input("Driver ID: ").strip()
        name = input("Name: ").strip()
        age = input("Age: ").strip()
        license_number = input("License Number: ").strip()
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        drivers = FileManager.load_drivers()

        # Check duplicate Driver ID
        for driver in drivers:
            data = driver.split(",")

            if data[0] == driver_id:
                print("\nDriver ID already exists.")
                return

        new_driver = ",".join([
            driver_id,
            name,
            age,
            license_number,
            username,
            password
        ])

        FileManager.add_driver(new_driver)

        print("\nDriver added successfully!")

    # --------------------------------------------------

    @staticmethod
    def update_driver():

        print("\n========== UPDATE DRIVER ==========")

        driver_id = input("Enter Driver ID: ").strip()

        drivers = FileManager.load_drivers()

        updated = False

        for i in range(len(drivers)):

            data = drivers[i].split(",")

            if data[0] == driver_id:

                print("\nLeave blank to keep existing value.\n")

                name = input(f"Name ({data[1]}): ").strip()
                age = input(f"Age ({data[2]}): ").strip()
                license_number = input(f"License ({data[3]}): ").strip()
                username = input(f"Username ({data[4]}): ").strip()
                password = input("Password: ").strip()

                if name:
                    data[1] = name

                if age:
                    data[2] = age

                if license_number:
                    data[3] = license_number

                if username:
                    data[4] = username

                if password:
                    data[5] = password

                drivers[i] = ",".join(data)

                updated = True
                break

        if updated:

            FileManager.save_drivers(drivers)

            print("\nDriver updated successfully!")

        else:

            print("\nDriver not found.")

    # --------------------------------------------------

    @staticmethod
    def delete_driver():

        print("\n========== DELETE DRIVER ==========")

        driver_id = input("Enter Driver ID: ").strip()

        drivers = FileManager.load_drivers()

        new_drivers = []

        found = False

        for driver in drivers:

            if driver.split(",")[0] == driver_id:
                found = True
            else:
                new_drivers.append(driver)

        if not found:

            print("\nDriver not found.")
            return

        FileManager.save_drivers(new_drivers)

        # Delete monitoring reports

        reports = FileManager.load_monitoring_reports()

        reports = [
            report for report in reports
            if report.split(",")[0] != driver_id
        ]

        FileManager.save_monitoring_reports(reports)

        # Delete alerts

        alerts = FileManager.load_alerts()

        alerts = [
            alert for alert in alerts
            if alert.split(",")[0] != driver_id
        ]

        FileManager.save_alerts(alerts)

        print("\nDriver deleted successfully!")

    # --------------------------------------------------

    @staticmethod
    def search_driver():

        print("\n========== SEARCH DRIVER ==========")

        driver_id = input("Enter Driver ID: ").strip()

        drivers = FileManager.load_drivers()

        for driver in drivers:

            data = driver.split(",")

            if data[0] == driver_id:

                obj = Driver(
                    data[0],
                    data[1],
                    int(data[2]),
                    data[3],
                    data[4],
                    data[5]
                )

                obj.display_profile()

                return

        print("\nDriver not found.")

    # --------------------------------------------------

    @staticmethod
    def view_all_drivers():

        print("\n========== ALL DRIVERS ==========")

        drivers = FileManager.load_drivers()

        if not drivers:

            print("No drivers available.")
            return

        for driver in drivers:

            data = driver.split(",")

            obj = Driver(
                data[0],
                data[1],
                int(data[2]),
                data[3],
                data[4],
                data[5]
            )

            obj.display_profile()

            print("-" * 40)