# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	data = get_all_value(filters)
	columns = get_columns()
	return columns, data

def get_all_value(filters):
	return frappe.db.get_all('Attendance' , ['employee_name','check_in', 'check_out', 'work_hours','late_hours'],filters = filters)

def get_columns():
	columns = [
		{'fieldname': 'employee_name', 'label':'Emplyee Name' , 'fieldtype':'Link' , 'options':'Employee' },
		{'fieldname': 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
		{'fieldname': 'check_in', 'label': 'Check in', 'fieldtype': 'Time'},
		{'fieldname': 'check_out', 'label': 'Check Out', 'fieldtype': 'Time'},
		{'fieldname': 'work_hours', 'label': 'Work Hours', 'fieldtype': 'float'},
		{'fieldname': 'late_hours', 'label': 'Late Hours', 'fieldtype': 'float'}]
	return columns
