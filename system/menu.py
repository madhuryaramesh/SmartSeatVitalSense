"""
Menu Module
Displays menus and controls program flow.
"""

from system.authentication import Authentication
from system.driver_manager import DriverManager
from system.monitoring import Monitoring
from system.report_generator import ReportGenerator


class Menu:

    def start(self):

        while True:

            print("\n======================================")
            print("     SMARTSEAT VITALSENSE SYSTEM")
            print("======================================")
            print("1. Admin Login")
            print("2. Driver Login")
            print("3. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                admin = Authentication.admin_login()

                if admin:
                    self.admin_menu()

            elif choice == "2":

                driver = Authentication.driver_login()

                if driver:
                    self.driver_menu(driver)

            elif choice == "3":

                print("\nThank you for using SmartSeat VitalSense.")
                break

            else:

                print("\nInvalid choice.")

    # ----------------------------------------------------

    def admin_menu(self):

        while True:

            print("\n========== ADMIN MENU ==========")
            print("1. Add Driver")
            print("2. Update Driver")
            print("3. Delete Driver")
            print("4. Search Driver")
            print("5. View All Drivers")
            print("6. View Monitoring Reports")
            print("7. View Alert Reports")
            print("8. Logout")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                DriverManager.add_driver()

            elif choice == "2":

                DriverManager.update_driver()

            elif choice == "3":

                DriverManager.delete_driver()

            elif choice == "4":

                DriverManager.search_driver()

            elif choice == "5":

                DriverManager.view_all_drivers()

            elif choice == "6":

                ReportGenerator.view_monitoring_reports()

            elif choice == "7":

                ReportGenerator.view_alert_reports()

            elif choice == "8":

                print("\nLogged out successfully.")
                break

            else:

                print("\nInvalid choice.")

    # ----------------------------------------------------

    def driver_menu(self, driver):

        while True:

            print("\n========== DRIVER MENU ==========")
            print("1. View My Profile")
            print("2. Start Monitoring")
            print("3. View My Monitoring Reports")
            print("4. View My Alerts")
            print("5. Logout")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                driver.display_profile()

            elif choice == "2":

                Monitoring.start_monitoring(driver)

            elif choice == "3":

                ReportGenerator.view_my_monitoring_reports(driver)

            elif choice == "4":

                ReportGenerator.view_my_alerts(driver)

            elif choice == "5":

                print("\nLogged out successfully.")
                break

            else:

                print("\nInvalid choice.")