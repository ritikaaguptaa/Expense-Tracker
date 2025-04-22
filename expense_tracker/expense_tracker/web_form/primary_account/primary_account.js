// frappe.ready(function () {
//     if (!frappe.web_form) return;

//     frappe.web_form.on('date_of_birth', (field, value) => {
//         if (!value) return;

//         const dob = new Date(value);
//         const today = new Date();
//         let age = today.getFullYear() - dob.getFullYear();
//         const m = today.getMonth() - dob.getMonth();

//         if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) {
//             age--;
//         }

// 		frappe.web_form.set_value('age', age);
//     });

//     function updateFullName() {
//         const first_name = frappe.web_form.get_value('first_name') || '';
//         const last_name = frappe.web_form.get_value('last_name') || '';
//         const full_name = `${first_name} ${last_name}`.trim();
//         frappe.web_form.set_value('full_name', full_name);
//     }

//     frappe.web_form.on('first_name', updateFullName);
//     frappe.web_form.on('last_name', updateFullName);
// });
const script = document.createElement("script");
script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
document.head.appendChild(script);


frappe.ready(function () {
    // Inject Premium Navy-Themed Styles
    const style = document.createElement('style');
    style.innerHTML = `
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(120deg,rgb(46, 61, 95),rgb(71, 96, 136));
            color: #f8fafc;
        }

        .web-form-wrapper {
            max-width: 720px;
            margin: 40px auto;
            background: #1e293b;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0px 12px 30px rgba(0, 0, 0, 0.4);
            animation: fadeIn 0.4s ease-in-out;
        }

        .web-form-header {
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            text-align: center;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 24px;
        }

        .control-label {
            font-size: 13px;
            font-weight: 500;
            color: #cbd5e1;
            margin-bottom: 6px;
        }

        .form-control {
            border-radius: 10px;
            border: 1px solid #334155;
            background-color: #0f172a;
            color: #f1f5f9;
            padding: 10px 14px;
            font-size: 14px;
            transition: border 0.2s ease, box-shadow 0.2s ease;
        }

        .form-control:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);
            background-color: #1e293b;
        }

        .btn-primary {
            background-color: #3b82f6;
            border: none;
            color: #ffffff;
            font-weight: 500;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 15px;
            transition: background-color 0.2s ease, transform 0.2s ease;
        }

        .frappe-control .selected-phone .country {
            color: #1e293b;
        }

        .btn-primary:hover {
            background-color: #2563eb;
            transform: translateY(-1px);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .success-page .success-body .success-message {
            color: #1e293b;
        }

        .phone-picker .search-phones input[type=search] {
            color: white;
        }

        .msgprint {
            color: #1e293b;
        }

    `;
    document.head.appendChild(style);

    // JS logic for auto-calculation and full name
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

    frappe.web_form.after_save = () => {
        if (typeof confetti === "function") {
            confetti({
                particleCount: 100,
                spread: 60,
                origin: { x: 0, y: 1 },
                angle: 60
            });
        
            confetti({
                particleCount: 100,
                spread: 60,
                origin: { x: 1, y: 1 },
                angle: 120
            });
        }
        

        frappe.show_alert({
            message: __('🎉 Registration successful!<br>Please check your email to complete your registration and start tracking your expenses.'),
            indicator: 'green'
        }, 7); 
    };

    frappe.web_form.on('first_name', updateFullName);
    frappe.web_form.on('last_name', updateFullName);
});
