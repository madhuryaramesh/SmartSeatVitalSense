"""
Report Generator Module
Displays monitoring and alert reports.
"""

from system.file_manager import FileManager


class ReportGenerator:

    # --------------------------------------------------
    # ADMIN REPORTS
    # --------------------------------------------------

    @staticmethod
    def view_monitoring_reports():

        print("\n========== MONITORING REPORTS ==========")

        reports = FileManager.load_monitoring_reports()

        if not reports:
            print("No monitoring reports found.")
            return

        for report in reports:

            data = report.split(",")

            print("-" * 60)
            print(f"Driver ID         : {data[0]}")
            print(f"Date              : {data[1]}")
            print(f"Posture           : {data[2]}")
            print(f"Sitting Duration  : {data[3]} minutes")
            print(f"Sleep Hours       : {data[4]}")
            print(f"Stress Level      : {data[5]}")
            print(f"Heart Rate        : {data[6]} bpm")
            print(f"Fatigue Level     : {data[7]}")
            print(f"Safety Score      : {data[8]}/100")

    # --------------------------------------------------

    @staticmethod
    def view_alert_reports():

        print("\n========== ALERT REPORTS ==========")

        alerts = FileManager.load_alerts()

        if not alerts:
            print("No alerts found.")
            return

        for alert in alerts:

            data = alert.split(",")

            print("-" * 50)
            print(f"Driver ID : {data[0]}")
            print(f"Date      : {data[1]}")
            print(f"Alert     : {data[2]}")
            print(f"Severity  : {data[3]}")

    # --------------------------------------------------
    # DRIVER REPORTS
    # --------------------------------------------------

    @staticmethod
    def view_my_monitoring_reports(driver):

        print("\n========== MY MONITORING REPORTS ==========")

        reports = FileManager.load_monitoring_reports()

        found = False

        for report in reports:

            data = report.split(",")

            if data[0] == driver.get_user_id():

                found = True

                print("-" * 60)
                print(f"Date              : {data[1]}")
                print(f"Posture           : {data[2]}")
                print(f"Sitting Duration  : {data[3]} minutes")
                print(f"Sleep Hours       : {data[4]}")
                print(f"Stress Level      : {data[5]}")
                print(f"Heart Rate        : {data[6]} bpm")
                print(f"Fatigue Level     : {data[7]}")
                print(f"Safety Score      : {data[8]}/100")

        if not found:
            print("No monitoring reports available.")

    # --------------------------------------------------

    @staticmethod
    def view_my_alerts(driver):

        print("\n========== MY ALERTS ==========")

        alerts = FileManager.load_alerts()

        found = False

        for alert in alerts:

            data = alert.split(",")

            if data[0] == driver.get_user_id():

                found = True

                print("-" * 50)
                print(f"Date      : {data[1]}")
                print(f"Alert     : {data[2]}")
                print(f"Severity  : {data[3]}")

        if not found:
            print("No alerts available.")