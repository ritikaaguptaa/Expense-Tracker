# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    # Define columns
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Distinct User Count", "fieldname": "user_count", "fieldtype": "Int", "width": 180},
    ]

    # Fetch distinct user count grouped by date
    data = frappe.db.sql("""
        SELECT
            DATE(`date`) AS `date`,
            COUNT(DISTINCT user_id) AS user_count
        FROM
            `tabExpense`
        GROUP BY
            DATE(`date`)
        ORDER BY
            `date` ASC
    """, as_dict=True)

    # Prepare chart data
    labels = [row["date"] for row in data]
    values = [row["user_count"] for row in data]

    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Distinct User Count",
                    "values": values
                }
            ]
        },
        "type": "line"
    }

    return columns, data, None, chart
