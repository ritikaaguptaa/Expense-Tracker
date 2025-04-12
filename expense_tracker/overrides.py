import frappe

def redirect_user_based_on_role(login_manager):
    user = frappe.session.user
    if user == "Administrator":
        frappe.local.response["home_page"] = "/app/dashboard-view/InsightHQ"
    else:
        frappe.local.response["home_page"] = "/app/"
