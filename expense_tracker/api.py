import frappe

@frappe.whitelist()
def get_expense_data():
    data = frappe.db.sql("""
        SELECT category, SUM(amount) as total FROM `tabExpenses`
        GROUP BY category
    """, as_dict=True)

    category_labels = [d['category'] for d in data]
    category_values = [d['total'] for d in data]

    total_expenses = sum(category_values)
    top_category = category_labels[category_values.index(max(category_values))] if category_labels else "-"
    total_transactions = frappe.db.count("Expenses")

    return {
        "total_expenses": total_expenses,
        "top_category": top_category,
        "total_transactions": total_transactions,
        "category_data": {
            "labels": category_labels,
            "values": category_values
        }
    }
