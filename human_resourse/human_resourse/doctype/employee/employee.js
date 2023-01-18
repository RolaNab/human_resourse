///////// date of birth ///////////
frappe.ui.form.on('Employee', {
 validate(frm) {
if (frm.doc.date_of_birth >= get_today()  ) {
//msgprint('You can not select date of birth after today');
 frappe.throw('You can not select date of birth after today');
}
} })
////////////// Age ///////////

frappe.ui.form.on('Employee', 'validate', function(frm) {
frm.set_df_property('age', 'read_only', '1');
    var today = new Date();
    var birthDate = new Date(frm.doc.date_of_birth);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    frm.set_value('age', age);
    if (age > 60) {
    frappe.msgprint("The Age more than 60 nnnn");
    Validate = false;
}
});

////////// Employee Number /////////////
frappe.ui.form.on('Employee',  {
 refresh: function(frm) {
 frm.set_df_property('employee_number', 'read_only',!frm.is_new());
 }
 });

/////////// Full Name /////////////
frappe.ui.form.on('Employee',  {
 refresh: function(frm) {
 frm.set_df_property('emplyee_full_name', 'read_only', '1');
 }
 });

 //////////// Employee Education /////////////


frappe.ui.form.on('Employee',  { validate: function(frm) {
 var total_education = 0;
 $.each(frm.doc.empolyee_education,  function(i,  d) {
 if ( d.school){
 total_education += 1; }
 });
frm.doc.count_employee_education = total_education;
}
 });

frappe.ui.form.on('Employee', {
 validate(frm) {
if (frm.doc.count_employee_education < 2 ) {
 frappe.throw('Employee Education must be have at least Two Education');
}
} })

///////////// Mobile Number ////////////
frappe.ui.form.on('Employee', 'validate', function(frm) {
if (frm.doc.mobile.length<10) {
frappe.msgprint("The Mobile Number is invalid");
Validate = false;
}
});
