"""
Monitoring Module
Handles driver monitoring, safety score calculation,
and alert generation.
"""

from datetime import datetime

from models.smart_seat import SmartSeat
from models.driving_session import DrivingSession
from models.alert import Alert

from system.file_manager import FileManager
from system.safety_score import SafetyScore


class Monitoring:

    @staticmethod
    def start_monitoring(driver):

        print("\n========== START MONITORING ==========")

        posture = input("Posture (Good/Poor): ").strip().title()

        sitting_duration = int(input("Sitting Duration (minutes): "))

        sleep_hours = float(input("Sleep Hours: "))

        stress_level = input(
            "Stress Level (Low/Medium/High): "
        ).strip().title()

        heart_rate = int(input("Heart Rate (bpm): "))

        fatigue_level = input(
            "Fatigue Level (Low/Medium/High): "
        ).strip().title()

        # Create SmartSeat object

        seat = SmartSeat(
            posture,
            sitting_duration,
            sleep_hours,
            stress_level,
            heart_rate,
            fatigue_level
        )

        # Calculate Safety Score

        score = SafetyScore.calculate_score(seat)

        # Current Date

        today = datetime.now().strftime("%Y-%m-%d")

        # Create Driving Session

        session = DrivingSession(
            driver.get_user_id(),
            today,
            posture,
            sitting_duration,
            sleep_hours,
            stress_level,
            heart_rate,
            fatigue_level,
            score
        )

        # Save Monitoring Report

        report = ",".join([
            session.get_driver_id(),
            session.get_date(),
            session.get_posture(),
            str(session.get_sitting_duration()),
            str(session.get_sleep_hours()),
            session.get_stress_level(),
            str(session.get_heart_rate()),
            session.get_fatigue_level(),
            str(session.get_safety_score())
        ])

        FileManager.add_monitoring_report(report)

        # Generate Alerts

        Monitoring.generate_alerts(driver, seat, today)

        print("\nMonitoring completed successfully.")
        print(f"Safety Score : {score}/100")

    # ---------------------------------------------------------

    @staticmethod
    def generate_alerts(driver, seat, today):

        driver_id = driver.get_user_id()

        if seat.get_posture() == "Poor":

            alert = Alert(
                driver_id,
                today,
                "Poor Posture",
                "Medium"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))

        if seat.get_sleep_hours() < 6:

            alert = Alert(
                driver_id,
                today,
                "Low Sleep",
                "High"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))

        if seat.get_stress_level() == "High":

            alert = Alert(
                driver_id,
                today,
                "High Stress",
                "High"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))

        if seat.get_heart_rate() > 100:

            alert = Alert(
                driver_id,
                today,
                "High Heart Rate",
                "High"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))

        if seat.get_fatigue_level() == "High":

            alert = Alert(
                driver_id,
                today,
                "Driver Fatigue",
                "High"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))

        if seat.get_sitting_duration() > 120:

            alert = Alert(
                driver_id,
                today,
                "Long Sitting Duration",
                "Medium"
            )

            FileManager.add_alert(",".join([
                alert.get_driver_id(),
                alert.get_date(),
                alert.get_alert_type(),
                alert.get_severity()
            ]))