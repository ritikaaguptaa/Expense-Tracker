frappe.ready(function () {
    if (!frappe.web_form) return;

    frappe.web_form.on('date_of_birth', (field, value) => {
        if (!value) return;

        const dob = new Date(value);
        const today = new Date();
        let age = today.getFullYear() - dob.getFullYear();
        const m = today.getMonth() - dob.getMonth();

        if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) {
            age--;
        }

		frappe.web_form.set_value('age', age);
    });
});
