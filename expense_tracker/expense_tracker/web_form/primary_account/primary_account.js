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

    function updateFullName() {
        const first_name = frappe.web_form.get_value('first_name') || '';
        const last_name = frappe.web_form.get_value('last_name') || '';
        const full_name = `${first_name} ${last_name}`.trim();
        frappe.web_form.set_value('full_name', full_name);
    }

    frappe.web_form.on('first_name', updateFullName);
    frappe.web_form.on('last_name', updateFullName);
});
