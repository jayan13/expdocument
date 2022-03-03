// Copyright (c) 2022, alantechnologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance', {
	refresh: function(frm) {
		
		if(frm.doc.policy_number){

			frm.add_custom_button(__('Renew'), function() {
			
				var new_item = frappe.model.copy_doc(frm.doc);
				// Duplicate item could have different name, causing "copy paste" error.
				if (new_item.policy_number===new_item.policy_number) {
					new_item.policy_number = null;
				}
				new_item.previous_policy_number=frm.doc.name;
				new_item.insurance_start_date='';
				new_item.insurance_end_date='';
				frappe.set_route('Form', 'Insurance', new_item.name);
			});

		}
	}
	
});
