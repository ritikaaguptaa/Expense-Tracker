# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from collections import defaultdict
from datetime import datetime

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Total Users Joined", "fieldname": "total_users", "fieldtype": "Int", "width": 150},
    ]

    user_counts = defaultdict(int)

    # Fetch creation dates from Primary Account
    primary_accounts = frappe.db.get_all(
        "Primary Account", 
        fields=["DATE(creation) as date"]
    )
    for entry in primary_accounts:
        user_counts[str(entry.date)] += 1

    # Fetch creation dates from Family Member
    family_members = frappe.db.get_all(
        "Family Member", 
        fields=["DATE(creation) as date"]
    )
    for entry in family_members:
        user_counts[str(entry.date)] += 1

    # Sort and format data
    sorted_dates = sorted(user_counts.keys(), key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
    data = [{"date": date, "total_users": user_counts[date]} for date in sorted_dates]

    # Add chart config
    chart = {
        "data": {
            "labels": [row["date"] for row in data],
            "datasets": [
                {
                    "name": "Users Joined",
                    "values": [row["total_users"] for row in data]
                }
            ]
        },
        "type": "line",  # can be 'bar', 'line', 'pie', etc.
        "colors": ["#007bff"]  # Optional: customize line color
    }

    return columns, data, None, chart
