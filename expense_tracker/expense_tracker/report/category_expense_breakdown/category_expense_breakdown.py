# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from collections import defaultdict

def execute(filters=None):
    columns = [
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 200},
        {"label": "Total Expenses", "fieldname": "total_expenses", "fieldtype": "Currency", "width": 150}
    ]

    expenses = frappe.get_list(
        "Expense",
        fields=["category", "amount"],
        ignore_permissions=False
    )

    category_totals = defaultdict(float)
    for expense in expenses:
        category = expense.get("category") or "Uncategorized"
        amount = expense.get("amount") or 0
        category_totals[category] += amount

    data = sorted(
        [{"category": cat, "total_expenses": total} for cat, total in category_totals.items()],
        key=lambda x: x["total_expenses"],
        reverse=True
    )

    return columns, data
