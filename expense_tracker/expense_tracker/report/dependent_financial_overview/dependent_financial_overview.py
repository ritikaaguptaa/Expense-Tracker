# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import datetime

def execute(filters=None):
    columns = [
        {"fieldname": "user_id", "label": _("User ID"), "fieldtype": "Link", "options": "User", "width": 150},
        {"fieldname": "pocket_money", "label": _("Pocket Money"), "fieldtype": "Currency", "width": 150},
        {"fieldname": "total_expenses", "label": _("Total Expenses This Month"), "fieldtype": "Currency", "width": 150}
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
    last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - datetime.timedelta(days=1))

    expenses = frappe.db.sql(
        """
        SELECT user_id, SUM(amount) AS total_expenses
        FROM `tabExpense`
        WHERE date >= %s AND date <= %s
        GROUP BY user_id
        """,
        (first_day_of_month, last_day_of_month),
        as_dict=True
    )

    pocket_money = frappe.get_all("Family Member", fields=["telegram_id", "pocket_money"])

    result = []
    expense_dict = {expense["user_id"]: expense["total_expenses"] for expense in expenses}
    pocket_money_dict = {member["telegram_id"]: member["pocket_money"] for member in pocket_money}

    user_ids = set(list(expense_dict.keys()) + list(pocket_money_dict.keys()))

    for user_id in user_ids:
        expense_amount = expense_dict.get(user_id, 0.0)
        pocket_amount = pocket_money_dict.get(user_id, 0.0)

        result.append({
            "user_id": user_id,
            "pocket_money": pocket_amount,
            "total_expenses": expense_amount
        })

    return result