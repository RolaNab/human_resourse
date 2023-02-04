// Copyright (c) 2023, Rola and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendence script report"] = {
	"filters": [
		{'fieldname': 'employee', 'label':'Emplyee Name' , 'fieldtype':'Link' , 'options':'Employee' },
		{'fieldname': 'attendance_date', 'label': 'Attendance Date ', 'fieldtype': 'Date'},

	]
};
