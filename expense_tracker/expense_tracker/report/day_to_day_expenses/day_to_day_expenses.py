# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt
import frappe
from collections import defaultdict
from datetime import datetime

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "User ID", "fieldname": "user_id", "fieldtype": "Data", "width": 180},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
    ]

    expenses = frappe.get_list(
        "Expense",
        fields=["date", "user_id", "amount"],
        ignore_permissions=False
    )

    aggregated_data = defaultdict(lambda: defaultdict(float))
    all_dates = set()
    user_ids = set()

    for row in expenses:
        if not row.date:
            continue

        date_str = row.date.strftime("%Y-%m-%d")
        user_id = row.user_id
        amount = row.amount or 0

        aggregated_data[user_id][date_str] += amount
        all_dates.add(date_str)
        user_ids.add(user_id)

    labels = sorted(all_dates)
    user_ids = sorted(user_ids)

    data = []
    for user_id in user_ids:
        for date in labels:
            total_amount = aggregated_data[user_id].get(date, 0)
            if total_amount:
                data.append({
                    "date": date,
                    "user_id": user_id,
                    "total_amount": total_amount
                })

    datasets = [
        {
            "name": user_id,
            "values": [aggregated_data[user_id].get(label, 0) for label in labels]
        } for user_id in user_ids
    ]

    chart = {
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "type": "line",
        "colors": ["#FF6B6B", "#4ECDC4", "#FFD93D", "#845EC2", "#2C73D2", "#F9A826", "#00C49A", "#F25C54", "#9D0191", "#F07B3F"]
    }

    return columns, data, None, chart
