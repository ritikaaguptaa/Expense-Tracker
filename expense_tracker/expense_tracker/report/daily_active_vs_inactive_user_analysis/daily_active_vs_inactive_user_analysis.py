# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Active Users", "fieldname": "active", "fieldtype": "Int", "width": 150},
        {"label": "Non-Active Users", "fieldname": "non_active", "fieldtype": "Int", "width": 180},
    ]

    # Daily active users
    active_data = frappe.db.sql("""
        SELECT 
            DATE(creation) as date,
            COUNT(DISTINCT user_id) as active
        FROM `tabExpense`
        WHERE user_id IS NOT NULL
        GROUP BY DATE(creation)
        ORDER BY DATE(creation)
    """, as_dict=True)

    # Total user count (Primary + Family)
    total_users = frappe.db.count("Primary Account") + frappe.db.count("Family Member")

    data = []
    for row in active_data:
        active = row.active
        non_active = max(0, total_users - active)  # avoid negatives

        data.append({
            "date": row.date,
            "active": active,
            "non_active": non_active
        })

    return columns, data
