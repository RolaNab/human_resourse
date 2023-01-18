# Copyright (c) 2023, Rola and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Employee(Document):
    def validate(self):
        self.fullName_()
        self.validate_age_()

    def fullName_(self):
        fName = self.emplyee_first_name
        mName = self.emplyee_middle_name
        lName = self.emplyee_last_name
        fullName = fName + " " + mName + " " + lName
        self.emplyee_full_name = fullName

    def validate_age_(self):
        if self.age > 60:
            return
