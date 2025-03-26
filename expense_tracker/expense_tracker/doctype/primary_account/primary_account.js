// Copyright (c) 2025, siddharth and contributors
// For license information, please see license.txt

frappe.ui.form.on('Primary Account', {
    refresh: function(frm) {
        if (!frm.is_new()) {  
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
                            reqd: 1,
                            options: 'Email'
                        }
                    ],
                    primary_action_label: 'Save',
                    primary_action(values) {
                        frappe.msgprint(
                            `<b>Dependent Added</b><br>
                            <b>Name:</b> ${values.full_name}<br>
                            <b>Email:</b> ${values.email}`
                        );

                        frappe.call({
                            method: 'expense_tracker.expense_tracker.doctype.primary_account.primary_account.send_email_to_dependent',
                            args: {
                                email: values.email,
                                name: values.full_name,
                                primary_name: frm.doc.full_name,
                                primary_id: frm.doc.name
                            },
                            callback: function(response) {
                                if (!response.exc) {
                                    frappe.msgprint(__('Email sent successfully to ' + values.email));
                                } else {
                                    frappe.msgprint(__('Failed to send email'));
                                }
                            }
                        });

                        d.hide();
                    }
                });
                d.show();
            });
        }
    }
});
