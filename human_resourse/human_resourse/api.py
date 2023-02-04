import frappe


@frappe.whitelist()
def get_all_employee(first_name=None):
    all_employee=[]
    if first_name:
        all_employee = frappe.db.sql(""" select * from `tabEmployee` where emplyee_first_name like %s""",first_name,as_dict=1)
    return all_employee

@frappe.whitelist()
def create_attendance( attendance_date=None , check_in=None , check_out=None):
    return  frappe.db.sql('''insert into tabAttendance (attendance_date, check_in, check_out)values(%s,%s,%s)'''
                                      , attendance_date,check_in,check_out)

