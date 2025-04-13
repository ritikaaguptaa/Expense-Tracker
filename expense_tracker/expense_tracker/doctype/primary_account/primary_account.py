# Copyright (c) 2025, Siddharth and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document
from frappe.utils.password import update_password

class PrimaryAccount(Document):
    def after_insert(self):
        self.create_user_with_role()
        self.assign_user_permission()

    def create_user_with_role(self):
        if not frappe.db.exists("User", self.email):

            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "roles": [{"role": "Expense Manager"}],
                "user_type": "System User"
            })
            user.insert(ignore_permissions=True)

    def assign_user_permission(self):
        user_permission = frappe.get_doc({
            "doctype": "User Permission",
            "user": self.email,
            "allow": "Primary Account",
            "for_value": self.name,
        })
        user_permission.insert(ignore_permissions=True)

@frappe.whitelist()
def send_email_to_dependent(email, name, primary_name, primary_id):
    subject = "You Have Been Added as a Dependent"
    message = f"""
<p>Dear {name},</p>
<p>Exciting news! <b>{primary_name}</b> has added you as a dependent.</p>
<p><b>Parent ID:</b> {primary_id}</p>
<p><b>Important:</b> Please do not share your Parent ID with anyone. You will be required to enter it after starting the bot.</p>
<p>Start managing your expenses with ease.</p>
<p>Click the link below and send the <b>/start</b> command to begin:</p>
<br>
<p style="text-align: center;">
    <a href="http://t.me/XpenseTrackrbot" target="_blank" 
       style="background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">
        🔗 Start Tracking Now
    </a>
</p>
<br>
<p>Need help? Feel free to reach out.</p>
<p>Best Regards,<br><b>Expense Tracker Team</b></p>
"""
    try:
        frappe.sendmail(
            recipients=[email],
            subject=subject,
            message=message
        )
        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
