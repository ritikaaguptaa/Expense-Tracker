// Copyright (c) 2025, siddharth and contributors
// For license information, please see license.txt

frappe.ui.form.on('Primary Account', {
    refresh: function(frm) {
        frm.add_custom_button(__('Add Dependent'), function() {
            let d = new frappe.ui.Dialog({
                title: 'Add Dependent',
                fields: [
                    {
                        label: 'Full Name',
                        fieldname: 'full_name',
                        fieldtype: 'Data',
                        reqd: 1
                    },
                    {
                        label: 'Email ID',
                        fieldname: 'email',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Save',
                primary_action(values) {
                    frappe.msgprint(
                        `<b>Dependent Added</b><br>
                        <b>Name:</b> ${values.full_name}<br>
                        <b>Email:</b> ${values.email}`
                    );
                    d.hide();
                }
            });
            d.show();
        });
    }
});






