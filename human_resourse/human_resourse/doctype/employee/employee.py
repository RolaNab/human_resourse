# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Employee(Document):
    def validate(self):
        self.fullName_()
        if not self.mobile.startswith('059'):
            frappe.throw('mobile number must start in 059')
    def fullName_(self):
        fName = self.emplyee_first_name
        mName = self.emplyee_middle_name
        lName = self.emplyee_last_name
        fullName = fName + " " + mName + " " + lName
        self.emplyee_full_name = fullName
