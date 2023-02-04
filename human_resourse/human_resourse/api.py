import frappe


@frappe.whitelist()
def get_all_employee(first_name=None):
    all_employee=[]
    if first_name:
        all_employee = frappe.db.sql(""" select * from `tabEmployee` where emplyee_first_name like %s""",first_name,as_dict=1)
    return all_employee

@frappe.whitelist(allow_guest=True)
def create_attendance(**kwargs):
    api_key = frappe.get_request_header("api-key")
    user = None
    if frappe.db.exists("User",{"api_key":api_key}):
        user = frappe.get_doc("User",{"api_key":api_key})
    if user:
        employee = frappe.get_doc("Employee",{"user":user.name})
        if 'attendance_date' not in kwargs or kwargs.get('attendance_date') == "":
            return "Invalid Input attendance_date"
        if 'check_in' not in kwargs or kwargs.get('check_in') == "":
            return "Invalid Input check_in"
        if 'check_out' not in kwargs or kwargs.get('check_out') == "":
            return "Invalid Input check_out"

        attendance = frappe.new_doc("Attendance")
        attendance.set('employee',employee.name)
        attendance.set('attendance_date',kwargs.get('attendance_date'))
        attendance.set('check_in',kwargs.get('check_in'))
        attendance.set('check_out',kwargs.get('check_out'))
        attendance.insert(ignore_permissions=True)
        frappe.db.commit()
        return "Attendance done successfully"

    else:
        return "Invalid User"
