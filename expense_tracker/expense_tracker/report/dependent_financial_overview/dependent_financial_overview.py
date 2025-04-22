# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from collections import defaultdict
import datetime

def execute(filters=None):
    columns = [
        {"fieldname": "user_id", "label": _("User ID"), "fieldtype": "Link", "options": "User", "width": 150},
        {"fieldname": "pocket_money", "label": _("Pocket Money"), "fieldtype": "Currency", "width": 150},
        {"fieldname": "total_expenses", "label": _("Total Expenses This Month"), "fieldtype": "Currency", "width": 180}
    ]

    data = get_monthly_expenses_and_pocket_money()

    chart = {
        "data": {
            "labels": [row["user_id"] for row in data],
            "datasets": [
                {
                    "name": "Pocket Money",
                    "values": [row["pocket_money"] for row in data]
                },
                {
                    "name": "Total Expenses",
                    "values": [row["total_expenses"] for row in data]
                }
            ]
        },
        "type": "bar",
        "colors": ["#7cd6fd", "#743ee2"],
        "axisOptions": {"xAxisMode": "tick", "yAxisMode": "span"},
        "height": 300
    }

    return columns, data, None, chart

def get_monthly_expenses_and_pocket_money():
    today = datetime.date.today()
    first_day_of_month = today.replace(day=1)
    if today.month == 12:
        last_day_of_month = today.replace(year=today.year + 1, month=1, day=1) - datetime.timedelta(days=1)
    else:
        last_day_of_month = today.replace(month=today.month + 1, day=1) - datetime.timedelta(days=1)


    expense_entries = frappe.get_list(
        "Expense",
        fields=["user_id", "amount", "date"],
        filters={
            "date": ["between", [first_day_of_month, last_day_of_month]]
        },
        ignore_permissions=False
    )

    expenses_by_user = defaultdict(float)
    for entry in expense_entries:
        user_id = entry.get("user_id")
        amount = entry.get("amount") or 0
        if user_id:
            expenses_by_user[user_id] += amount

    pocket_money_list = frappe.get_list(
        "Family Member",
        fields=["telegram_id", "pocket_money"],
        ignore_permissions=False
    )

    pocket_by_user = {member["telegram_id"]: member["pocket_money"] for member in pocket_money_list}

    user_ids = set(expenses_by_user.keys()) | set(pocket_by_user.keys())

    result = []
    for user_id in user_ids:
        result.append({
            "user_id": user_id,
            "pocket_money": pocket_by_user.get(user_id, 0),
            "total_expenses": expenses_by_user.get(user_id, 0)
        })

    return result
