# Copyright (c) 2025, siddharth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FamilyMember(Document):
    def validate(self):
        if not self.telegram_id.isdigit() or not (9 <= len(self.telegram_id) <= 12):
            frappe.throw("Telegram ID must be a numeric value between 9 and 12 digits.")
