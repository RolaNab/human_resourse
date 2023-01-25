// Copyright (c) 2023, Rola and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leave Application', {
	 validate: function(frm) {
        if (frm.doc.from_date < get_today()) {
            frappe.throw(__("Please select a From Date from the present or future."));
        }
    },
});
