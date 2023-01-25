# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt
from typing import Dict, Optional, Tuple
import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, getdate, cstr, formatdate
from frappe import _




class LeaveAllocation(Document):
	def validate(self):
		self.check_dates()
		self.validate_leave_overlap()
	def check_dates(self):
		if self.from_date and self.to_date and (getdate(self.to_date) < getdate(self.from_date)):
			frappe.throw(_("To date cannot be before from date"))

	# def check_leave_duplication(self):
	# 	self.check_dates()
	# 	if self.employee and self.from_date and self.to_date :
	# 		leave_allocated = frappe.db.sql(""" select total_leaves_allocated from `tabLeave Allocation`
	# 		where employee = %s
	# 		and (from_date between %(from_date)s and %(to_date)s
	# 		or to_date between %(from_date)s and %(to_date)s
	# 		or %(from_date)s between from_date and to_date)""", (self.employee,self.from_date, self.to_date), as_dict=1)
	#
	# 		if leave_allocated:
	# 			frappe.throw('this leave is duplicated for employee ' + self.employee_name)




	def validate_leave_overlap(self):
		if not self.name:
			self.name = "New Leave Application"

		for d in frappe.db.sql("""select name,
			from_date, to_date
			from `tabLeave Application`
			where
			employee = %(employee)s
			and (from_date between %(from_date)s and %(to_date)s
				or to_date between %(from_date)s and %(to_date)s
				)
			and name != %(name)s""", {
			"employee": self.employee,
			"from_date": self.from_date,
			"to_date": self.to_date,
			"name": self.name
		}, as_dict = 1):
			frappe.msgprint(
				_("Employee {0} has already applied for leave between {1} and {2} ").format(
					self.employee_name,formatdate(d['from_date']), formatdate(d['to_date'])))
			frappe.throw('<a href="#Form/Leave Application/{0}">{0}</a>'.format(d["name"]))
