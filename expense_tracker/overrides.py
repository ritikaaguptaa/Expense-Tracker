import frappe

def redirect_user_based_on_role():
    user = frappe.session.user
    if user == "Administrator":
        frappe.local.response["home_page"] = "/dashboard-view/InsightHQ"
    else:
        print("edsfsfslse\n\n\n")
        frappe.local.response["home_page"] = "/app"
