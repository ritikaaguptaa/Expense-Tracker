# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    user = frappe.session.user

    salary = frappe.db.get_value(
        "Primary Account",
        {"email": user},
        "salary"
    ) or 0  # If salary not found, set to 0

    columns = [
        {
            "fieldname": "salary",
            "label": "Available Balance",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = [{"salary": salary}]

    return columns, data
