import frappe

def monthly_pocket_money_scheduler():
    family_members = frappe.get_all("Family Member", fields=["name", "pocket_money", "rollover_savings", "primary_account"])
    
    for member in family_members:
        new_roll_over = member.roll_over_savings + member.pocket_money
        
        frappe.db.set_value("Family Member", member.name, {
            "rollover_savings": new_roll_over,
            "pocket_money": 0
        })
    
    primary_accounts = frappe.get_all("Primary Account", fields=["name", "total_expenses", "default_pocket_money"])
    
    for account in primary_accounts:
        frappe.db.set_value("Primary Account", account.name, "total_expenses", 0)
    
    for account in primary_accounts:
        family_members = frappe.get_all("Family Member", filters={"primary_account_holder": account.name}, fields=["name"])
        
        for member in family_members:
            frappe.db.set_value("Family Member", member.name, "pocket_money", account.default_pocket_money_for_dependents)
        
        total_expenses = account.default_pocket_money_for_dependents * len(family_members)
        frappe.db.set_value("Primary Account", account.name, "total_expense", total_expenses)
    
    frappe.db.commit()
