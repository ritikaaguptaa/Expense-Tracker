import frappe
from frappe.model.document import Document

class FamilyMember(Document):
    def validate(self):
        if self.telegram_id:
            if not self.telegram_id.isdigit() or not (9 <= len(self.telegram_id) <= 12):
                frappe.throw("Telegram ID must be a numeric value between 9 and 12 digits.")
