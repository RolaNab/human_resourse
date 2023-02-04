# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import time_diff
from frappe.model.document import Document
from datetime import datetime, timedelta


class Attendance(Document):
	def validate(self):
		self.calculate_work_hours()

	def on_submit(self):
		self.calculate_work_hours()

	def calculate_work_hours(self):
		late_entry = frappe.db.get_single_value("Attendance Settings", "late_entry_grace_period")
		start_time_single1 = frappe.db.get_single_value("Attendance Settings", "start_time")

		early_exit_single = frappe.db.get_single_value("Attendance Settings", "early_exit_grace_period")
		end_time_single = frappe.db.get_single_value("Attendance Settings", "end_time")

		working_hours_threshold_for_absent = frappe.db.get_single_value("Attendance Settings", "working_hours_threshold_for_absent")

		total_start = start_time_single1 + timedelta(minutes=late_entry)
		total_end_time = end_time_single - timedelta(minutes=early_exit_single)

		check_in = datetime.strptime(self.check_in, "%H:%M:%S")
		check_out = datetime.strptime(self.check_out, "%H:%M:%S")

		check_total_start = datetime.strptime(str(total_start), "%H:%M:%S")
		check_total_end = datetime.strptime(str(total_end_time), "%H:%M:%S")

		check_start_date = datetime.strptime(str(start_time_single1), "%H:%M:%S")
		check_end_date = datetime.strptime(str(end_time_single), "%H:%M:%S")

		if check_in < check_start_date:
			check_in = check_start_date
		if check_out > check_end_date:
			check_out = check_end_date

		all_period = check_end_date - check_start_date
		sec = all_period.total_seconds()
		hours = sec / (60 * 60)

		if check_in >= check_start_date and check_in <= check_total_start and check_out <= check_end_date and check_out >= check_total_end:
			check_in = check_start_date
			check_out = check_end_date
			delta1 = check_out - check_in
			sec = delta1.total_seconds()
			hours1 = sec / (60 * 60)
			self.work_hours = hours1
			self.late_hours = hours - hours1
		elif check_in >= check_start_date and check_in >= check_total_start:
			check_in = check_in - timedelta(minutes=late_entry)
			check_out = check_out+ timedelta(minutes=early_exit_single)
			delta2 = check_out - check_in
			sec = delta2.total_seconds()
			hours2 = sec / (60 * 60)
			self.work_hours = hours2
			self.late_hours = hours - hours2
		elif check_out <= check_end_date and check_out <= check_total_end:
			check_in = check_in - timedelta(minutes=late_entry)
			check_out = check_out + timedelta(minutes=early_exit_single)
			delta2 = check_out - check_in
			sec = delta2.total_seconds()
			hours2 = sec / (60 * 60)
			self.work_hours = hours2
			self.late_hours = hours - hours2
		else:
			check_in = check_in - timedelta(minutes=late_entry)
			check_out = check_out + timedelta(minutes=early_exit_single)
			delta2 = check_out - check_in
			sec = delta2.total_seconds()
			hours2 = sec / (60 * 60)
			self.work_hours = hours2
			self.late_hours = hours - hours2

		if self.work_hours <= working_hours_threshold_for_absent:
			self.status = 'Absent'
		else:
			self.status = 'Present'

# @frappe.whitelist()
# def calculate_work_hours(check_in,check_out):
# 		# start time and end time
# 		start_time = datetime.strptime(check_in , "%H:%M:%S")
# 		end_time = datetime.strptime(check_out , "%H:%M:%S")
# 		delta = end_time - start_time
# 		sec = delta.total_seconds()
# 		hours = sec / (60 * 60)
# 		return hours