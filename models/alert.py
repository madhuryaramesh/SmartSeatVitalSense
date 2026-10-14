"""
Alert Class
Stores alert information generated during monitoring.
"""


class Alert:
    """Represents one driver alert."""

    def __init__(self, driver_id, date,
                 alert_type, severity):

        self._driver_id = driver_id
        self._date = date
        self._alert_type = alert_type
        self._severity = severity

    # ---------- Getters ----------

    def get_driver_id(self):
        return self._driver_id

    def get_date(self):
        return self._date

    def get_alert_type(self):
        return self._alert_type

    def get_severity(self):
        return self._severity

    # ---------- Display ----------

    def display_alert(self):
        """Display alert information."""

        print("\n========== ALERT ==========")
        print(f"Driver ID : {self._driver_id}")
        print(f"Date      : {self._date}")
        print(f"Alert     : {self._alert_type}")
        print(f"Severity  : {self._severity}")