# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Employee(Document):
    def validate(self):
        return
        self.fullName_()

    def fullName_(self):
        return
    #     fName = self.emplyee_first_name
    #     mName = self.emplyee_middle_name
    #     lName = self.emplyee_last_name
    #     fullName = fName + " " + mName + " " + lName
    #     self.emplyee_full_name = fullName