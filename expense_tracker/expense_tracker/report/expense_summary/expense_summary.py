# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
    try:
        if not filters or not filters.get("chat_id"):
            frappe.throw("Chat ID is required to generate the report.")

        chat_id = filters.get("chat_id")
        current_year = datetime.now().year

        columns = [
            {"label": "Month", "fieldname": "month", "fieldtype": "Data", "width": 120},
            {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 150},
            {"label": "Total Amount", "fieldname": "total", "fieldtype": "Currency", "width": 150},
        ]

        data = frappe.db.sql("""
            SELECT
                DATE_FORMAT(date, '%M') AS month,
                category,
                SUM(amount) AS total
            FROM `tabExpense`
            WHERE
                YEAR(date) = %s AND
                user_id = %s
            GROUP BY MONTH(date), category
            ORDER BY MONTH(date), category
        """, (current_year, chat_id), as_dict=True)

        return columns, data

    except Exception as e:
        frappe.log_error(frappe.as_json(e), "Report Query Error")
        frappe.msgprint(f"An error occurred while fetching report data: {e}", indicator='error')
        return [], []
