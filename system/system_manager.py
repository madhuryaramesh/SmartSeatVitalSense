"""
System Manager Module
Main controller for the SmartSeat VitalSense system.
"""

from system.driver_manager import DriverManager
from system.monitoring import Monitoring
from system.report_generator import ReportGenerator


class SystemManager:

    @staticmethod
    def add_driver():
        DriverManager.add_driver()

    @staticmethod
    def update_driver():
        DriverManager.update_driver()

    @staticmethod
    def delete_driver():
        DriverManager.delete_driver()

    @staticmethod
    def search_driver():
        DriverManager.search_driver()

    @staticmethod
    def view_all_drivers():
        DriverManager.view_all_drivers()

    @staticmethod
    def start_monitoring(driver):
        Monitoring.start_monitoring(driver)

    @staticmethod
    def view_monitoring_reports():
        ReportGenerator.view_monitoring_reports()

    @staticmethod
    def view_alert_reports():
        ReportGenerator.view_alert_reports()

    @staticmethod
    def view_my_monitoring_reports(driver):
        ReportGenerator.view_my_monitoring_reports(driver)

    @staticmethod
    def view_my_alerts(driver):
        ReportGenerator.view_my_alerts(driver)