# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "User ID", "fieldname": "user_id", "fieldtype": "Data", "width": 180},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
    ]

    # Extract only the DATE part from the datetime field
    data = frappe.db.sql("""
        SELECT 
            DATE(date) as date,
            user_id,
            SUM(amount) as total_amount
        FROM `tabExpense`
        GROUP BY user_id, DATE(date)
        ORDER BY DATE(date)
    """, as_dict=True)

    # Get distinct sorted date labels
    labels = sorted(list(set(row["date"].strftime("%Y-%m-%d") for row in data)))

    # Collect unique user_ids
    user_ids = list(set(row["user_id"] for row in data))

    # Map user_ids to date -> amount
    user_data_map = {user: {label: 0 for label in labels} for user in user_ids}

    for row in data:
        date_str = row["date"].strftime("%Y-%m-%d")
        user_data_map[row["user_id"]][date_str] = row["total_amount"]

    # Prepare chart datasets
    datasets = [
        {
            "name": user_id,
            "values": [user_data_map[user_id][label] for label in labels]
        } for user_id in user_ids
    ]

    # Final chart config
    chart = {
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "type": "line",
        "colors": ["#FF6B6B", "#4ECDC4", "#FFD93D", "#845EC2", "#2C73D2", "#F9A826", "#00C49A", "#F25C54", "#9D0191", "#F07B3F"]
    }

    return columns, data, None, chart
