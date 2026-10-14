"""
File Manager Module
Handles all file input and output operations.
"""

class FileManager:

    DRIVER_FILE = "data/drivers.txt"
    ADMIN_FILE = "data/admins.txt"
    MONITORING_FILE = "data/monitoring_reports.txt"
    ALERT_FILE = "data/alerts.txt"

    # ---------------------------------------------------------
    # DRIVER FILE
    # ---------------------------------------------------------

    @staticmethod
    def load_drivers():
        """Return all drivers as a list."""

        drivers = []

        try:
            with open(FileManager.DRIVER_FILE, "r") as file:

                for line in file:
                    line = line.strip()

                    if line:
                        drivers.append(line)

        except FileNotFoundError:
            pass

        return drivers

    @staticmethod
    def save_drivers(drivers):
        """Rewrite drivers.txt."""

        with open(FileManager.DRIVER_FILE, "w") as file:

            for driver in drivers:
                file.write(driver + "\n")

    @staticmethod
    def add_driver(driver):
        """Append one driver."""

        with open(FileManager.DRIVER_FILE, "a+") as file:
            file.seek(0)

            content = file.read()

            if content and not content.endswith("\n"):
                file.write("\n")

            file.write(driver + "\n")

    # ---------------------------------------------------------
    # MONITORING REPORTS
    # ---------------------------------------------------------

    @staticmethod
    def load_monitoring_reports():
        """Return all monitoring reports."""

        reports = []

        try:
            with open(FileManager.MONITORING_FILE, "r") as file:

                for line in file:
                    line = line.strip()

                    if line:
                        reports.append(line)

        except FileNotFoundError:
            pass

        return reports

    @staticmethod
    def save_monitoring_reports(reports):
        """Rewrite monitoring_reports.txt."""

        with open(FileManager.MONITORING_FILE, "w") as file:

            for report in reports:
                file.write(report + "\n")

    @staticmethod
    def add_monitoring_report(report):
        """Append one monitoring report."""

        with open(FileManager.MONITORING_FILE, "a") as file:
            file.write(report + "\n")

    # ---------------------------------------------------------
    # ALERTS
    # ---------------------------------------------------------

    @staticmethod
    def load_alerts():
        """Return all alerts."""

        alerts = []

        try:
            with open(FileManager.ALERT_FILE, "r") as file:

                for line in file:
                    line = line.strip()

                    if line:
                        alerts.append(line)

        except FileNotFoundError:
            pass

        return alerts

    @staticmethod
    def save_alerts(alerts):
        """Rewrite alerts.txt."""

        with open(FileManager.ALERT_FILE, "w") as file:

            for alert in alerts:
                file.write(alert + "\n")

    @staticmethod
    def add_alert(alert):
        """Append one alert."""

        with open(FileManager.ALERT_FILE, "a") as file:
            file.write(alert + "\n")